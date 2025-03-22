import os
import feedparser
from serpapi import GoogleSearch
from APIkeys import get_api_key


#SERPAPI_KEY = os.getenv("SERPAPI_KEY")
SERPAPI_KEY = get_api_key("SERPAPI_KEY")
if not SERPAPI_KEY:
    raise ValueError("ERROR: SERPAPI_KEY is missing! Set it in your environment variables.")


def get_google_news(topic):
    """Fetch 5 trending topics from Google News via RSS."""
    print("🔎 Fetching Google News...")
    url = f"https://news.google.com/rss/search?q={topic.replace(' ', '+')}"
    try:
        feed = feedparser.parse(url)
        return [(entry.title, entry.link) for entry in feed.entries[:5]]
    except Exception as e:
        print(f"❌ Error fetching Google News: {e}")
        return []

def get_bing_news(topic):
    """Fetch 5 trending topics from Bing News using SerpAPI."""
    if not SERPAPI_KEY:
        print("Warning: API_KEY is missing! Bing News will be skipped.")
        return []

    print("🔎 Fetching Bing News from SerpAPI...")

    params = {
        "engine": "bing_news",  
        "q": topic,
        "cc": "us",
        "api_key": SERPAPI_KEY  
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results.get("organic_results", [])

        # Ensure Bing results match the Google News format (title, link)
        bing_results = [
            (article["title"], article.get("link", "No Link Available"))  # Extract title and link
            for article in organic_results[:5]
        ]
    except Exception as e:
        print(f"❌ Error fetching Bing News: {e}")
        return []

    return bing_results



def research_topic(topic):
    """Fetch topics from both Google News & Bing News."""
    google_news = get_google_news(topic)
    bing_news = get_bing_news(topic)
    all_news = list(set(google_news + bing_news))
    #all_news = google_news
    if not all_news:
        return "No research data found."

    return "\n".join(f" {title}\n  {link}" for title, link in all_news)


    
