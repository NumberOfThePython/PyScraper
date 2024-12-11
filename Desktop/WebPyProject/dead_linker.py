import requests

def check_dead_link(url):
    try:
        response = requests.get(url)
        if response.status_code 200:
            return f"Link działa: {url}"
        else:
            return f"Błąd {response.status_code} dla: {url}"
    except requests.exceptions.RequestException as e:
        return f"Błąd połączenia z {url}: {e}"