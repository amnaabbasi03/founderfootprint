# scrape_utils.py
import os
import requests
from newspaper import Article
from dotenv import load_dotenv

load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")


def get_articles_for_person(name, company=None, num_results=5):
    query = name
    if company:
        query += f" {company}"

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": num_results,
        "hl": "en",
        "gl": "us"
    }

    search_url = "https://serpapi.com/search"
    res = requests.get(search_url, params=params)
    results = res.json()

    links = []
    if "organic_results" in results:
        for result in results["organic_results"]:
            if "link" in result:
                links.append(result["link"])

    articles = []
    for url in links:
        try:
            article = Article(url)
            article.download()
            article.parse()
            if article.text.strip():
                articles.append({
                    "url": url,
                    "text": article.text.strip()
                })
        except Exception as e:
            print(f"Failed to parse {url}: {e}")
            continue

    return articles

