import requests
from bs4 import BeautifulSoup
from utils import fetch_url, parse_html, extract_data

def get_valid_url(default_url):
    """
    Prompt the user for a URL. If left blank, use the default.
    If the URL is invalid or unreachable, prompt again.
    """
    while True:
        user_input = input(
            f"Enter the URL to scrape (leave blank to use default: {default_url}):\n> "
        ).strip()
        url = user_input if user_input else default_url

        print(f"Attempting to fetch: {url}")
        html_content = fetch_url(url)
        if html_content is not None:
            return url, html_content
        else:
            print("Invalid or unreachable URL. Please enter a valid URL.\n")

def main():
    """
    My Cat Web Scraper
    Fetches a webpage, parses HTML, and extracts headings and intro paragraphs.
    Demonstrates robust error handling and clear code structure.
    """
    default_url = "https://webscraper.io/test-sites/tables"

    # Prompt user for URL and fetch content
    url, html_content = get_valid_url(default_url)

    # Parse the HTML content
    soup = parse_html(html_content)
    if soup is None:
        print("Failed to parse HTML content. Exiting.")
        return

    # Extract data: all <h1> headings and <p class="intro"> paragraphs
    headings = extract_data(soup, 'h1')
    paragraphs = extract_data(soup, 'p', class_name='intro')

    # Output the collected data
    print("\nHeadings found:")
    if headings:
        for h in headings:
            print(f"- {h}")
    else:
        print("No <h1> headings found.")

    print("\nIntro Paragraphs found:")
    if paragraphs:
        for p in paragraphs:
            print(f"- {p}")
    else:
        print("No <p class='intro'> paragraphs found.")

if __name__ == "__main__":
    main()