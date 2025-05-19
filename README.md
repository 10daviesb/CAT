# CAT - Web Scraping Project

## Overview
CAT is a beginner-friendly Python project for practicing web scraping concepts. It demonstrates how to make HTTP requests, parse HTML, extract data from webpages, and now includes advanced features such as multi-page scraping, data export, automated analysis, and visualization. The script is interactive, robust, and well-documented, making it suitable for both learning and assessment purposes.

## Features
- **Interactive URL Input:** Prompts the user for one or more URLs, a filename containing URLs, or uses a clear default if left blank.
- **Multi-Page Scraping:** Supports scraping multiple pages in one run, either from a comma-separated list or a file.
- **Robust HTTP Requests:** Uses the `requests` library to fetch web content, handling status codes and network errors gracefully.
- **Flexible HTML Parsing:** Utilizes `BeautifulSoup` to parse HTML and extract elements, with code that is resilient to minor HTML changes.
- **Data Extraction:** Extracts all `<h1>` headings and `<p class="intro">` paragraphs, but can be easily adapted for other elements.
- **Error Handling:** Provides clear feedback for invalid URLs, unreachable pages, and missing HTML elements.
- **Data Export:** Saves results for all pages to CSV or JSON in an `output/` folder, with customizable filenames.
- **Automated Data Analysis:** Counts and summarizes the number of headings and intro paragraphs per page.
- **Data Visualization:** Displays a bar chart comparing the number of headings and intro paragraphs for each page using `matplotlib`.
- **Modular Code:** Separates concerns into utility functions (`utils.py`), a main script (`main.py`), and tests (`tests/`).
- **Unit Testing:** Includes automated tests for core utility functions to ensure reliability.
- **Clear Documentation:** Includes docstrings and comments explaining each step and decision.

## Project Structure
```
CAT
├── src
│   ├── main.py        # Main script to initiate web scraping, analysis, and visualization
│   └── utils.py       # Utility functions for HTTP requests and HTML parsing
├── tests
│   └── test_utils.py  # Unit tests for utility functions
├── output             # Folder for exported CSV/JSON results
├── requirements.txt   # List of project dependencies
└── README.md          # Project documentation
```

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone https://github.com/10daviesb/CAT.git
   cd CAT
   ```

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the web scraping script, execute:
```
python src/main.py
```
You will be prompted to enter one or more URLs to scrape (comma-separated), a filename containing URLs, or leave blank to use the default test URL. The script will fetch each page, parse its HTML, and extract all `<h1>` headings and `<p class="intro">` paragraphs, displaying them in the console.

After scraping, you can:
- **Export results** to CSV or JSON in the `output/` folder.
- **View a summary** of the number of headings and intro paragraphs per page.
- **See a bar chart** comparing these counts across all pages.

## How It Works
- **HTTP Requests:**  
  The script uses `requests.get()` to fetch each webpage. It checks the response status and handles exceptions, ensuring the user is notified of any issues.
- **HTML Parsing:**  
  `BeautifulSoup` parses the HTML content, allowing for flexible and robust extraction of elements.
- **Data Extraction:**  
  Utility functions are used to find all elements of a given type (e.g., headings or paragraphs with a specific class) and extract their text content.
- **Error Handling:**  
  If the user enters an invalid or unreachable URL, the script explains the issue and skips to the next. If no relevant HTML elements are found, the script notifies the user.
- **Data Export:**  
  All results are aggregated and can be saved to CSV or JSON, with each row or entry including the source URL.
- **Analysis & Visualization:**  
  The script prints a summary table and displays a bar chart of the number of headings and intro paragraphs per page.
- **Testing:**  
  The `tests/` folder contains unit tests for the utility functions, which can be run with `python -m unittest tests/test_utils.py`.

## Example Output
```
Enter URLs to scrape (comma-separated), a filename, or leave blank for default (https://webscraper.io/test-sites/tables):
> https://webscraper.io/test-sites/tables, https://example.com

Attempting to fetch: https://webscraper.io/test-sites/tables
...
Results for https://webscraper.io/test-sites/tables:
Headings found:
- Test Sites
Intro Paragraphs found:
No <p class='intro'> paragraphs found.

--- Data Analysis ---
https://webscraper.io/test-sites/tables
  Headings: 1
  Intro Paragraphs: 0
https://example.com
  Headings: 1
  Intro Paragraphs: 0

[Bar chart appears here]
```

## Dependencies
- `requests`: For making HTTP requests to fetch web pages.
- `beautifulsoup4`: For parsing HTML and extracting data.
- `matplotlib`: For data visualization.

## Notes
- The script is designed to be robust against minor changes in HTML structure.
- All code is clearly commented to explain the approach and logic.
- The project demonstrates best practices in error handling, modularity, user interaction, data analysis, and visualization.

## License
This project is open-source and available under the MIT License.
