import unittest
import sys
import os

# Ensure the src directory is in the path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils import fetch_url, parse_html, extract_data

class TestUtils(unittest.TestCase):
    def test_fetch_url_valid(self):
        # Should return HTML content for a valid URL
        html = fetch_url("https://webscraper.io/test-sites/tables")
        self.assertIsInstance(html, str)
        self.assertIn("<html", html.lower())

    def test_fetch_url_invalid(self):
        # Should return None for an invalid URL
        html = fetch_url("http://invalid.url.abc/")
        self.assertIsNone(html)

    def test_parse_html(self):
        html = "<html><body><h1>Hello</h1></body></html>"
        soup = parse_html(html)
        self.assertEqual(soup.h1.text, "Hello")

    def test_extract_data(self):
        html = "<html><body><h1>Title</h1><p class='intro'>Intro</p></body></html>"
        soup = parse_html(html)
        headings = extract_data(soup, "h1")
        intros = extract_data(soup, "p", class_name="intro")
        self.assertEqual(headings, ["Title"])
        self.assertEqual(intros, ["Intro"])

if __name__ == "__main__":
    unittest.main()