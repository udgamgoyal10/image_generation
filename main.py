import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from pprint import pprint

pprint(types.GenerateImagesConfig.model_fields)              # lists allowed fields + types
st.title("🖼️ Google Gemini Image Generator")

# --- API key securely (from env var or Streamlit secrets)
api_key = st.secrets.get("GEMINI_API_KEY", None)
if not api_key:
    st.error("❌ API key not found. Please set GEMINI_API_KEY in your environment or Streamlit secrets.")
    st.stop()

# --- Initialize Google GenAI client
client = genai.Client(api_key=api_key)

# --- Prompt input
prompt = st.text_area("Enter your prompt:")

# --- Model selection
model = st.selectbox(
    "Select a Google image generation model:",
    [
        "imagen-4.0-generate-001",
        "imagen-4.0-ultra-generate-001",
        "imagen-4.0-fast-generate-001",
        "imagen-3.0-generate-002"
    ]
)

sampleImageSize = st.selectbox(
    "Select image quality:",
    [
        "1K",
        "2K"
    ]
)

aspectRatio = st.selectbox(
    "Select aspect ratio:",
    [
        "1:1", 
        "3:4",
        "4:3",
        "9:16",
        "16:9"
    ]
)


# --- Number of images
num_images = st.slider("Number of images", 1, 4, 1)

# --- Generate button
if st.button("Generate Image"):
    if not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        try:
            with st.spinner("Generating image..."):
                # Generate the images
                response = client.models.generate_images(
                    model=model,
                    prompt=prompt,
                    config=types.GenerateImagesConfig(
                        number_of_images= num_images,
                        image_size=sampleImageSize,
                        aspect_ratio=aspectRatio
                    )
                )

                if response.generated_images:
                    for i, generated_image in enumerate(response.generated_images):
                        try:
                            # Based on the attributes we discovered, we can access image_bytes directly
                            # from the image object
                            image_bytes = generated_image.image.image_bytes
                            
                            # Create a PIL Image from the bytes
                            img = Image.open(BytesIO(image_bytes))
                            
                            # Display the image
                            st.image(img, caption=f"Result {i+1}", width="stretch")
                            
                            # Create download button
                            buffer_out = BytesIO()
                            img.save(buffer_out, format="PNG")
                            buffer_out.seek(0)
                            st.download_button(
                                label=f"Download Result {i+1}",
                                data=buffer_out.getvalue(),
                                file_name=f"result_{i+1}.png",
                                mime="image/png"
                            )
                            
                        except Exception as img_error:
                            st.error(f"Error processing image {i+1}: {str(img_error)}")
                            
                            # More detailed error information
                            if hasattr(generated_image, 'model_dump'):
                                try:
                                    image_dict = generated_image.model_dump()
                                    st.write("Image model dump keys:", list(image_dict.keys()))
                                    st.write("Image type:", type(image_dict.get('image')))
                                    
                                    # Try direct display as a last resort
                                    if 'image' in image_dict and isinstance(image_dict['image'], bytes):
                                        st.write("Attempting direct display of bytes...")
                                        st.image(BytesIO(image_dict['image']), caption=f"Result {i+1} (direct bytes)")
                                except Exception as dump_error:
                                    st.error(f"Error accessing model_dump: {str(dump_error)}")
                            
                            # Print more details about the object for debugging
                            st.error(f"Image object type: {type(generated_image)}")
                            if hasattr(generated_image, 'image'):
                                st.error(f"Image attribute type: {type(generated_image.image)}")
                                # Try to get more info about the image object
                                st.error(f"Image attributes: {dir(generated_image.image)}")
                                
                                # Try to get the model_dump of the image
                                try:
                                    if hasattr(generated_image.image, 'model_dump'):
                                        image_dump = generated_image.image.model_dump()
                                        st.write("Image dump:", image_dump)
                                except:
                                    st.error("Could not get model_dump of image")



                else:
                    st.error("No images returned. Check your quota or prompt.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
