from flask import Flask, request, render_template, jsonify
from groq import Groq
import base64
import mimetypes
import requests

app = Flask(__name__)
client = Groq(api_key="groq apikey https://console.groq.com/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nsfw", methods=["POST"])
def nsfw_check():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    image_data = base64.b64encode(image.read()).decode("utf-8")
    data_url = f"data:{image.mimetype};base64,{image_data}"

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a strict NSFW image classifier.\n"
                    "Your response must follow this exact format without any variation:\n"
                    "yes(XX%)[short description] or no(XX%)[short description]\n"
                    "- XX% is your confidence (integer only).\n"
                    "- Description must be inside square brackets.\n"
                    "- Do NOT include any periods, punctuation, or words outside this format.\n"
                    "- Do NOT add extra words before or after.\n"
                    "- Do NOT explain anything.\n"
                    "- Example valid responses: yes(73%)[woman wearing lingerie], no(92%)[a cat sitting on the floor]"
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Is this an NSFW image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": data_url
                        }
                    }
                ]
            }
        ],
        temperature=0.2,
        max_completion_tokens=64,
        top_p=1,
        stream=False,
        stop=None,
    )

    result = response.choices[0].message.content.strip()
    return jsonify({"result": result})

@app.route("/convert-url", methods=["POST"])
def convert_image_url():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "Missing 'url' field"}), 400

    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            return jsonify({"error": "Failed to download image"}), 400

        content_type = resp.headers.get("Content-Type")
        if not content_type:
            content_type = mimetypes.guess_type(url)[0] or "image/jpeg"

        b64_data = base64.b64encode(resp.content).decode("utf-8")
        data_url = f"data:{content_type};base64,{b64_data}"
        return jsonify({"data_url": data_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
