import logging
from urllib.parse import urljoin

import requests
import pandas as pd
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_soup(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch {url}: {e}")
        return None

def parse_books(soup):
    records = []
    products = soup.find_all("article", class_="product_pod")

    for product in products:
        h3 = product.find("h3")
        h3_anchor = h3.find("a") if h3 else None
        title = h3_anchor["title"] if h3_anchor and h3_anchor.has_attr("title") else None

        price_tag = product.find("p", class_="price_color")
        price = price_tag.text if price_tag else None

        if title and price:
            records.append({
                "title": title.strip(),
                "price": price.strip()
            })
    return records

def run():
    logging.info("Starting web scraper pipeline.")

    # Trailing slash matters so urljoin keeps /catalogue/ in the path
    start_url = "https://books.toscrape.com/catalogue/page-1.html"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    all_records = []
    target_url = start_url

    while target_url:
        logging.info(f"Scraping: {target_url}")

        soup = get_soup(target_url, headers)
        if not soup:
            break

        all_records.extend(parse_books(soup))

        next_button = soup.find("li", class_="next")
        next_link = next_button.find("a") if next_button else None
        # Resolve relative href (e.g. "page-2.html") against the current page URL
        target_url = urljoin(target_url, next_link["href"]) if next_link else None

    if not all_records:
        logging.warning("No records extracted. Aborting pipeline.")
        return

    df = pd.DataFrame(all_records)
    df["price"] = df["price"].str.replace("£", "", regex=False).astype(float)
    df.rename(columns={"price": "price_gbp"}, inplace=True)

    output_file = "sanitized_product_feed.csv"
    df.to_csv(output_file, index=False, encoding="utf-8")
    logging.info(f"Successfully exported {len(df)} rows to {output_file}")

if __name__ == "__main__":
    run()
    input("\nPress ENTER to exit...")