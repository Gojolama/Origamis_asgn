import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """Scrapes the given URL and extracts clean text from its body."""
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Raise error if request fails

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract main text from common HTML tags
        paragraphs = soup.find_all(["p", "span", "div"], text=True)
        text = "\n".join([p.get_text(strip=True) for p in paragraphs])

        return text
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"