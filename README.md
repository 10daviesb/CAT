# CAT - Web Scraping Project

## Overview
<<<<<<< HEAD
CAT is a beginner-friendly Python project for practicing web scraping concepts. It demonstrates how to make HTTP requests, parse HTML, and extract data from a webpage. The script is interactive, robust, and well-documented, making it suitable for both learning and assessment purposes.

## Features
- **Interactive URL Input:** Prompts the user for a URL, with a clear default if left blank.
- **Robust HTTP Requests:** Uses the `requests` library to fetch web content, handling status codes and network errors gracefully.
- **Flexible HTML Parsing:** Utilizes `BeautifulSoup` to parse HTML and extract elements, with code that is resilient to minor HTML changes.
- **Data Extraction:** Extracts all `<h1>` headings and `<p class="intro">` paragraphs, but can be easily adapted for other elements.
- **Error Handling:** Provides clear feedback for invalid URLs, unreachable pages, and missing HTML elements.
- **Modular Code:** Separates concerns into utility functions (`utils.py`) and a main script (`main.py`) for clarity and maintainability.
- **Clear Documentation:** Includes docstrings and comments explaining each step and decision.
=======
CAT is a beginner-friendly project designed to help users practice basic web scraping concepts. The project focuses on making HTTP requests, parsing HTML, and extracting data from a specified webpage. The goal is to fetch information such as text or data tables from a URL and output the collected data in a usable format.
>>>>>>> 144daa185fd312b24bfc810216e17dd86b0216d6

## Project Structure
```
CAT
├── src
│   ├── main.py        # Main script to initiate web scraping
│   └── utils.py       # Utility functions for HTTP requests and HTML parsing
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
You will be prompted to enter a URL to scrape. If you leave it blank, the script will use a default test URL. The script will fetch the page, parse its HTML, and extract all `<h1>` headings and `<p class="intro">` paragraphs, displaying them in the console.

## How It Works
- **HTTP Requests:**  
  The script uses `requests.get()` to fetch the webpage. It checks the response status and handles exceptions, ensuring the user is notified of any issues.
- **HTML Parsing:**  
  `BeautifulSoup` parses the HTML content, allowing for flexible and robust extraction of elements.
- **Data Extraction:**  
  Utility functions are used to find all elements of a given type (e.g., headings or paragraphs with a specific class) and extract their text content.
- **Error Handling:**  
  If the user enters an invalid or unreachable URL, the script explains the issue and prompts again. If no relevant HTML elements are found, the script notifies the user.
- **Extensibility:**  
  The code is structured so that extracting different elements or saving output to a file can be added with minimal changes.

## Example Output
```
Enter the URL to scrape (leave blank to use default: https://webscraper.io/test-sites/tables):
> 
Attempting to fetch: https://webscraper.io/test-sites/tables

Headings found:
- Test Tables

Intro Paragraphs found:
No <p class='intro'> paragraphs found.
```

## Dependencies
- `requests`: For making HTTP requests to fetch web pages.
- `beautifulsoup4`: For parsing HTML and extracting data.

## Notes
- The script is designed to be robust against minor changes in HTML structure.
- All code is clearly commented to explain the approach and logic.
- The project demonstrates best practices in error handling, modularity, and user interaction.

## License
This project is open-source and available under the MIT License.
