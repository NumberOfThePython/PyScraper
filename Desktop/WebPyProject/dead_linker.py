import requests
from bs4 import BeautifulSoup


def get_all_links(url):
    # Apka pobiera Hrefy ze strony
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a.get("href") for a in soup.find_all("a", href=True)]
        # dodawane linki muszę być pełne w formacie http
        links = [link if link.startswith("http") else f"{url.rstrip('/')}/{link.lstrip('/')}" for link in links]
        return links
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching the URL: {e}")


def check_link_statuses(links):
    # sprawdzenie statusu linka

    results = []
    for link in links:
        try:
            response = requests.head(link, allow_redirects=True, timeout=5)

            statuses[link] = response.status_code
        except requests.exceptions.RequestException:
            statuses[link] = "Nieznany błąd."
    return statuses