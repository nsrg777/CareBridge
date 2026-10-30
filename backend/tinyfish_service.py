from tinyfish import TinyFish
from dotenv import load_dotenv
from pathlib import Path
import os

# Load environment variables
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)

# Initialize TinyFish
client = TinyFish(
    api_key=os.getenv("TINYFISH_API_KEY")
)


def search_healthcare(query):

    response = client.search.query(
        query=query,
        location="IN",
        language="en"
    )

    results = []

    for item in response.results:

        results.append({
            "title": item.title,
            "url": item.url,
            "snippet": item.snippet
        })

    return results
