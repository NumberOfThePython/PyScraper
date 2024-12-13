import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

def get_all_links(url):
   #Apka pobiera Hrefy ze strony
   try:
       response = requests.get(url)
       response.raise_for_status()
       soup = BeautifulSoup(response.text, "html.parser")
       links = [a.get("href") for a in soup.find_all("a", href=True)]
       links = [link if link.startswith("http") else f"{url.rstrip('/')}/{link.lstrip('/')}" for link in links]

       print(f"Znaleziono linki: {links}")  # Logowanie do debugowania
       return links
   except requests.exceptions.RequestException as e:
       raise Exception(f"Problem ze sprawdzeniem linka: {e}")

def check_link_statuses(links):

    #sprawdzenie statusu linka

    statuses = {}
    for link in links:
        try:
            response = requests.get(link, allow_redirects=True, timeout=10, headers=HEADERS)
            if response.status_code != 200:
                statuses[link] = response.status_code
        except requests.exceptions.RequestException as e:
            statuses[link] = f"Błąd: {e}"  # Logujemy szczegóły błędu
    return statuses


