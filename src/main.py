import os
import requests
from bs4 import BeautifulSoup
from utils import fetch_url, parse_html, extract_data
import csv
import json
import matplotlib.pyplot as plt

def get_urls(default_url):
    """
    Prompt the user for URLs (comma-separated) or a filename containing URLs.
    If left blank, use the default.
    """
    user_input = input(
        f"Enter URLs to scrape (comma-separated), a filename, or leave blank for default ({default_url}):\n> "
    ).strip()
    if not user_input:
        return [default_url]
    if os.path.isfile(user_input):
        with open(user_input, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    # Otherwise, treat as comma-separated URLs
    return [url.strip() for url in user_input.split(",") if url.strip()]

def export_data(all_results):
    """
    Save the aggregated data to CSV or JSON in the 'output' folder.
    """
    if not all_results:
        print("No data to export.")
        return

    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)

    choice = input("\nWould you like to save the results? (csv/json/skip): ").strip().lower()
    if choice == "csv":
        filename = input("Enter filename for CSV (default: output.csv): ").strip() or "output.csv"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["URL", "Type", "Content"])
            for result in all_results:
                url = result["url"]
                for h in result["headings"]:
                    writer.writerow([url, "Heading", h])
                for p in result["intro_paragraphs"]:
                    writer.writerow([url, "Intro Paragraph", p])
        print(f"Data saved to {filepath}")
    elif choice == "json":
        filename = input("Enter filename for JSON (default: output.json): ").strip() or "output.json"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(all_results, f, ensure_ascii=False, indent=2)
        print(f"Data saved to {filepath}")
    else:
        print("Skipping data export.")

def analyze_and_visualize(all_results):
    """
    Analyze and visualize the number of headings and intro paragraphs per URL.
    """
    urls = [result["url"] for result in all_results]
    heading_counts = [len(result["headings"]) for result in all_results]
    intro_counts = [len(result["intro_paragraphs"]) for result in all_results]

    print("\n--- Data Analysis ---")
    for url, h_count, i_count in zip(urls, heading_counts, intro_counts):
        print(f"{url}\n  Headings: {h_count}\n  Intro Paragraphs: {i_count}")

    # Visualization
    x = range(len(urls))
    plt.figure(figsize=(10, 5))
    plt.bar(x, heading_counts, width=0.4, label='Headings', align='center')
    plt.bar(x, intro_counts, width=0.4, label='Intro Paragraphs', align='edge')
    plt.xticks(x, [f"Page {i+1}" for i in x], rotation=45)
    plt.xlabel('Pages')
    plt.ylabel('Count')
    plt.title('Headings and Intro Paragraphs per Page')
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    """
    My Cat Web Scraper (Multi-page & Automated)
    Fetches one or more webpages, parses HTML, and extracts headings and intro paragraphs.
    Demonstrates scalability, automation, and basic data analysis/visualization.
    """
    default_url = "https://webscraper.io/test-sites/tables"
    urls = get_urls(default_url)
    all_results = []

    for url in urls:
        print(f"\nAttempting to fetch: {url}")
        html_content = fetch_url(url)
        if html_content is None:
            print(f"Failed to retrieve {url}. Skipping.")
            continue

        soup = parse_html(html_content)
        if soup is None:
            print(f"Failed to parse HTML for {url}. Skipping.")
            continue

        headings = extract_data(soup, 'h1')
        paragraphs = extract_data(soup, 'p', class_name='intro')

        print(f"\nResults for {url}:")
        print("Headings found:")
        if headings:
            for h in headings:
                print(f"- {h}")
        else:
            print("No <h1> headings found.")

        print("Intro Paragraphs found:")
        if paragraphs:
            for p in paragraphs:
                print(f"- {p}")
        else:
            print("No <p class='intro'> paragraphs found.")

        all_results.append({
            "url": url,
            "headings": headings,
            "intro_paragraphs": paragraphs
        })

    export_data(all_results)
    if all_results:
        analyze_and_visualize(all_results)

if __name__ == "__main__":
    main()