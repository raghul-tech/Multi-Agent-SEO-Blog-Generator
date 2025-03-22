import os
import time
import google.generativeai as genai
from APIkeys import get_api_key

#this will get the gemini api from the environment variable
#API_KEY = os.getenv("GEMINI_API_KEY")
API_KEY = get_api_key("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("ERROR: GEMINI_API_KEY is missing! Set it in your environment variables.")

genai.configure(api_key=API_KEY)
# this is to generate content from gemini with retry 
def generate_response(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
            return response.text
        except Exception as e:
            print(f" Error: {e}. Retrying ({attempt + 1}/{retries})...")
            time.sleep(2)
    return " Content generation failed."