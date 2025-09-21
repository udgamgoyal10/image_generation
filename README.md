# Google Gemini Image Generator

A Streamlit web application that uses Google's Gemini API to generate images based on text prompts.

## Features

- Generate images using Google's Gemini API
- Select from different Imagen models
- Choose the number of images to generate
- Download generated images

## Local Setup

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

## Deployment on Streamlit Cloud

1. Fork or push this repository to your GitHub account

2. Sign in to [Streamlit Cloud](https://streamlit.io/cloud)

3. Click on "New app" and select your repository

4. Set the following:
   - **Repository**: `your-username/image_generation`
   - **Branch**: `master` (or `main` if you prefer)
   - **Main file path**: `main.py`

5. Under "Advanced settings", add your secrets:
   - Click on "Secrets"
   - Add your Google Gemini API key in the following format:
     ```toml
     GEMINI_API_KEY = "your-api-key-here"
     ```

6. Click "Deploy"

7. Your app should now be deployed and accessible via the provided URL

## Troubleshooting Deployment

- **ImportError**: If you encounter an import error for the Google GenAI package, make sure your Streamlit Cloud instance is using the correct Python version (3.9+ recommended).

- **API Key Issues**: Verify that your API key is correctly set in the Streamlit Cloud secrets management.

- **Branch Issues**: If Streamlit Cloud can't find your branch, make sure you're using the correct branch name (`master` or `main`).

## Usage

1. Enter a descriptive prompt for the image you want to generate
2. Select the Gemini model to use
3. Choose the number of images to generate
4. Click "Generate Image"
5. Download the generated images using the download buttons

## Requirements

- Python 3.9+
- Streamlit 1.32.0+
- Google GenAI Python SDK 0.7.0+
- PIL (Pillow) 10.1.0+
