# NSFW Detector

This is an open-source NSFW (Not Safe For Work) image detection web application powered by a simple API. It allows users to upload an image file or provide an image URL, and then detects whether the image contains NSFW content.

---

## How the Website Works

The front-end interface lets users either:

- Upload an image file from their device  
- Or enter a direct image URL

Upon submission, the website will:

1. If an image URL is provided:
   - Send a POST request to the `/convert-url` API endpoint with the URL.
   - The server converts the URL into image data (base64 encoded), returning it as `data_url`.
   - The client converts this data URL into a `Blob` to send it as a file.

2. If an image file is uploaded directly:
   - The client uses the file as-is.

3. The image file/blob is sent via a POST request to the `/nsfw` API endpoint.

4. The `/nsfw` endpoint returns a JSON response with a `result` string indicating:
   - Whether the image is NSFW ("yes" or "no")
   - The confidence percentage
   - Optionally, a textual description of the detection.

The result is then displayed on the webpage with clear color-coded feedback.

---

## API Endpoints

### 1. POST `/convert-url`

- **Description**: Converts an image URL into a base64 data URL that can be sent for NSFW detection.
- **Request Body**: JSON
  ```json
  {
    "url": "https://example.com/image.jpg"
  }
  ```
