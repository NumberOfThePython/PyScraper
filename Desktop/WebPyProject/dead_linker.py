import requests
from bs4 import BeautifulSoup

def get_all_links(url):
   #Apka pobiera Hrefy ze strony
    try:
        response = requests.get(url)
        response.raise_for_status()  # Wyjątek jeśli strona odpowie błędem
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a.get("href") for a in soup.find_all("a", href=True)]
        # Filtrowanie linków: upewnij się, że linki są absolutne
        links = [link if link.startswith("http") else f"{url.rstrip('/')}/{link.lstrip('/')}" for link in links]
        return links
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching the URL: {e}")

def check_link_statuses(links):
    """
    Sprawdza status kodu HTTP.
    """
    statuses = {}
    for link in links:
        try:
            response = requests.head(link, allow_redirects=True, timeout=5)
            statuses[link] = response.status_code
        except requests.exceptions.RequestException:
            statuses[link] = "Błąd"
    return statuses