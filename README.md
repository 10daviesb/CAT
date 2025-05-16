# CAT - Web Scraping Project

## Overview
CAT is a beginner-friendly project designed to help users practice basic web scraping concepts. The project focuses on making HTTP requests, parsing HTML, and extracting data from a specified webpage. The goal is to fetch information such as text or data tables from a URL and output the collected data in a usable format.

## Project Structure
```
my-cat
├── src
│   ├── main.py        # Main script to initiate web scraping
│   └── utils.py       # Utility functions for HTTP requests and HTML parsing
├── requirements.txt    # List of project dependencies
└── README.md           # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/10daviesb/CAT.git
   cd CAT
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the web scraping script, execute the following command:
```
python src/main.py
```

Make sure to modify the URL in `src/main.py` to the webpage you want to scrape.

## Dependencies
This project requires the following Python packages:
- `requests`: For making HTTP requests to fetch web pages.
- `beautifulsoup4`: For parsing HTML and extracting data.

## Example
An example of how to use the functions in `utils.py` will be provided in the `main.py` file. The script will demonstrate how to handle HTTP responses, parse HTML content, and extract specific data elements.

## License
This project is open-source and available under the MIT License.
