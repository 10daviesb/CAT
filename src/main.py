import os
import requests
from bs4 import BeautifulSoup
from utils import fetch_url, parse_html, extract_data
import csv
import json
import matplotlib.pyplot as plt

def get_urls(default_url):
    """
    Prompt the user for URLs to scrape.

    The user can enter:
    - A comma-separated list of URLs,
    - A filename containing URLs (one per line),
    - Or leave blank to use the provided default URL.

    Args:
        default_url (str): The default URL to use if input is blank.

    Returns:
        list[str]: List of URLs to scrape.
    """
    user_input = input(
        f"Enter URLs to scrape (comma-separated), a filename, or leave blank for default ({default_url}):\n> "
    ).strip()
    if not user_input:
        return [default_url]
    if os.path.isfile(user_input):
        with open(user_input, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    return [url.strip() for url in user_input.split(",") if url.strip()]

def export_data(all_results):
    """
    Save the aggregated scraping results to CSV or JSON in the 'output' folder.

    Prompts the user for the desired format and filename.
    Each row/entry includes the source URL, element type, and content.

    Args:
        all_results (list[dict]): List of result dictionaries for each URL.
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
            writer.writerow(["URL", "Element", "Content"])
            for result in all_results:
                url = result["url"]
                for key in result:
                    if key == "url":
                        continue
                    for item in result[key]:
                        writer.writerow([url, key, item])
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
    Analyze and visualize the number of each extracted element per URL.

    Prints a summary table and displays a bar chart comparing element counts across all pages.

    Args:
        all_results (list[dict]): List of result dictionaries for each URL.
    """
    if not all_results:
        print("No data to analyze.")
        return

    # Get all dynamic element keys (excluding 'url')
    element_keys = set()
    for result in all_results:
        element_keys.update(k for k in result if k != "url")
    element_keys = sorted(element_keys)

    print("\n--- Data Analysis ---")
    for result in all_results:
        print(f"{result['url']}")
        for key in element_keys:
            count = len(result.get(key, []))
            print(f"  {key}: {count}")

    # Visualization: bar chart for each element type per page
    import numpy as np
    urls = [result["url"] for result in all_results]
    x = np.arange(len(urls))
    width = 0.8 / len(element_keys) if element_keys else 0.8

    plt.figure(figsize=(10, 5))
    for idx, key in enumerate(element_keys):
        counts = [len(result.get(key, [])) for result in all_results]
        plt.bar(x + idx * width, counts, width=width, label=key)
    plt.xticks(x + width * (len(element_keys)-1)/2, [f"Page {i+1}" for i in x], rotation=45)
    plt.xlabel('Pages')
    plt.ylabel('Count')
    plt.title('Extracted Elements per Page')
    plt.legend()
    plt.tight_layout()
    plt.show()

def get_elements_to_extract():
    """
    Prompt the user for HTML elements (and optional classes) to extract.

    The user can specify:
    - Just an element (e.g., 'h1')
    - An element with a class (e.g., 'p.intro')
    - Multiple, separated by commas (e.g., 'h1, p.intro, table')

    Returns:
        list[tuple[str, str or None]]: List of (element, class_name) pairs.
    """
    print("\nSpecify which HTML elements to extract.")
    print("Format: element or element.classname (e.g., h1 or p.intro). Separate multiple with commas.")
    print("Leave blank for default: h1, p.intro")
    user_input = input("> ").strip()
    if not user_input:
        return [("h1", None), ("p", "intro")]
    elements = []
    for part in user_input.split(","):
        part = part.strip()
        if "." in part:
            element, class_name = part.split(".", 1)
            elements.append((element.strip(), class_name.strip()))
        else:
            elements.append((part, None))
    return elements

def main():
    """
    Main entry point for the My Cat Web Scraper.

    - Prompts the user for URLs and elements to extract.
    - Scrapes each page, extracting the specified elements.
    - Displays results, offers to export, and visualizes the data.
    """
    default_url = "https://webscraper.io/test-sites/tables"
    urls = get_urls(default_url)
    elements_to_extract = get_elements_to_extract()
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

        result = {"url": url}
        for element, class_name in elements_to_extract:
            key = f"{element}{'.' + class_name if class_name else ''}"
            result[key] = extract_data(soup, element, class_name=class_name)
            print(f"\n{key} found:")
            if result[key]:
                for item in result[key]:
                    print(f"- {item}")
            else:
                print(f"No <{element}{' class=' + class_name if class_name else ''}> elements found.")
        all_results.append(result)

    export_data(all_results)
    if all_results:
        analyze_and_visualize(all_results)

if __name__ == "__main__":
    main()