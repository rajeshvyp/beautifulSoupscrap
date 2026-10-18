
import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    page = requests.get(URL, headers=headers, timeout=10)
    page.raise_for_status()

    soup = BeautifulSoup(page.text, "html.parser")

    # Find possible headline elements
    items = soup.select("h2")

    headlines = []
    seen = set()

    for item in items:
        headline = item.get_text(" ", strip=True)

        if headline and headline not in seen:
            headlines.append(headline)
            seen.add(headline)

        if len(headlines) == 5:
            break

    if headlines:
        for i, headline in enumerate(headlines, start=1):
            print(f"{i}. {headline}")
    else:
        print("No headlines found. Check the HTML selector.")

except requests.RequestException as error:
    print(f"Error fetching the news page: {error}")
