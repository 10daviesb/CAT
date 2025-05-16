def fetch_url(url):
    import requests

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(html_content):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def extract_data(soup, element, class_name=None):
    if class_name:
        data = soup.find_all(element, class_=class_name)
    else:
        data = soup.find_all(element)

    return [item.get_text(strip=True) for item in data]