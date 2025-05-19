import os
import requests
from bs4 import BeautifulSoup
from utils import fetch_url, parse_html, extract_data
import csv
import json

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

def export_data(headings, paragraphs):
    """
    Prompt the user to save the extracted data to CSV or JSON in the 'output' folder.
    """
    if not headings and not paragraphs:
        print("No data to export.")
        return

    # Ensure the output directory exists
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)

    choice = input("\nWould you like to save the results? (csv/json/skip): ").strip().lower()
    if choice == "csv":
        filename = input("Enter filename for CSV (default: output.csv): ").strip() or "output.csv"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Type", "Content"])
            for h in headings:
                writer.writerow(["Heading", h])
            for p in paragraphs:
                writer.writerow(["Intro Paragraph", p])
        print(f"Data saved to {filepath}")
    elif choice == "json":
        filename = input("Enter filename for JSON (default: output.json): ").strip() or "output.json"
        filepath = os.path.join(output_dir, filename)
        data = {
            "headings": headings,
            "intro_paragraphs": paragraphs
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Data saved to {filepath}")
    else:
        print("Skipping data export.")

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

    # Offer to export data
    export_data(headings, paragraphs)

if __name__ == "__main__":
    main()