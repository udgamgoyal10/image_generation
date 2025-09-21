# Google Gemini Image Generator

A Streamlit web application that uses Google's Gemini API to generate images based on text prompts.

## Features

- Generate images using Google's Gemini API
- Select from different Imagen models
- Choose the number of images to generate
- Download generated images

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/udgamgoyal10/image_generation.git
   cd image_generation
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.streamlit/secrets.toml` file with your Google Gemini API key:
   ```
   GEMINI_API_KEY = "your-api-key-here"
   ```

4. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

## Usage

1. Enter a descriptive prompt for the image you want to generate
2. Select the Gemini model to use
3. Choose the number of images to generate
4. Click "Generate Image"
5. Download the generated images using the download buttons

## Requirements

- Python 3.7+
- Streamlit
- Google GenAI Python SDK
- PIL (Pillow)
