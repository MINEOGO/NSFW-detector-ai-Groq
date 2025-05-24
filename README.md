# NSFW Detector API

An open-source NSFW image detection API powered by Groq AI. This API allows you to check images for NSFW content by either uploading an image file or providing an image URL.

---

## Features

- Detect NSFW content in images
- Accepts image uploads or image URLs
- Returns confidence and detailed description
- Simple JSON API responses

---

## Base URL

The API base URL depends on your deployment. For example:

```
https://yourdomain.com/
```

---

## Endpoints

### 1. POST `/convert-url`

Convert an image URL into a base64-encoded data URL.

- **Request:**

  ```json
  {
    "url": "https://example.com/image.jpg"
  }
  ```

- **Response:**

  ```json
  {
    "data_url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
  }
  ```

- **Description:**  
  This endpoint fetches the image from the provided URL, converts it into a base64 data URL for further processing.

---

### 2. POST `/nsfw`

Analyze an image and determine if it contains NSFW content.

- **Request:**

  Form-data body with key `image`:

  - Upload an image file directly  
  **OR**  
  - Upload a base64 data URL image as a Blob (e.g. result of `/convert-url`)

- **Response:**

  ```json
  {
    "result": "yes (95%) [explicit adult content]"
  }
  ```

  or

  ```json
  {
    "result": "no (5%) [safe]"
  }
  ```

- **Description:**  
  Returns if the image is NSFW or not, the confidence percentage, and an optional description of the content.

---

### 3. GET `/health`

Simple health check endpoint.

- **Response:**

  ```json
  {
    "status": "ok"
  }
  ```

---

## Usage Example

Here is a sample usage in JavaScript (browser):

```js
// Upload an image file
const formData = new FormData();
formData.append('image', yourImageFile);

const response = await fetch('/nsfw', {
  method: 'POST',
  body: formData
});
const result = await response.json();
console.log(result.result); // e.g. "yes (95%) [explicit adult content]"
```

Or convert a URL and then send to `/nsfw`:

```js
const urlResponse = await fetch('/convert-url', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ url: 'https://example.com/image.jpg' })
});
const urlData = await urlResponse.json();

const blob = dataURLtoBlob(urlData.data_url);
const nsfwForm = new FormData();
nsfwForm.append('image', blob, 'image_from_url.jpg');

const nsfwResponse = await fetch('/nsfw', { method: 'POST', body: nsfwForm });
const nsfwResult = await nsfwResponse.json();
console.log(nsfwResult.result);
```

---

## Response Format

The `result` field in JSON contains a string with this pattern:

```
<yes|no> (<confidence>%) [optional description]
```

- `yes` means NSFW detected  
- `no` means safe content  
- `confidence` is a percentage of certainty  
- `optional description` gives additional context

---

## Error Handling

Errors return a JSON response with an `error` field describing the issue, e.g.:

```json
{
  "error": "Invalid URL format provided."
}
```

---

## License

This project is open source and licensed under the MIT License.
