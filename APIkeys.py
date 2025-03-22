import os

# Dictionary to store API keys with placeholders
api_keys = {
    "GEMINI_API_KEY": "your_Gemini_api_key",
    "SERPAPI_KEY": "your_serpapi_Bing_news_api"
}

# Function to retrieve API key based on ID
def get_api_key(api_id):
    return api_keys.get(api_id, "Invalid API ID")

