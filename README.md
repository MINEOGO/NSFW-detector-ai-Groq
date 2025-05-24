# NSFW Detector API & Web Interface

A simple and efficient NSFW (Not Safe For Work) image detection API and frontend web interface powered by the **Groq NSFW detection API**.

Users can upload images or submit image URLs to detect NSFW content with confidence scores and optional content descriptions.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [API Endpoints](#api-endpoints)  
- [Usage](#usage)  
- [Installation](#installation)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Overview

This project provides:

- A clean web UI for users to upload images or submit URLs for NSFW detection.
- A RESTful API backend that processes images and returns NSFW classification using Groq API.
- Image URL conversion to Base64 for easy processing.
- Clear and detailed JSON responses indicating NSFW status, confidence, and tags.

---

## Features

- Upload image files for NSFW detection.
- Submit publicly accessible image URLs.
- Get quick responses with confidence percentages.
- Detailed NSFW content description tags.
- Easy-to-use REST API compatible with any client.
- Simple frontend interface included.

---

## API Endpoints

### 1. POST `/convert-url`

**Purpose:** Converts a publicly accessible image URL into a Base64 encoded data URL for further NSFW detection.

- **Request Headers:**  
  `Content-Type: application/json`

- **Request Body:**  
  ```json
  {
    "url": "https://example.com/image.jpg"
  }
