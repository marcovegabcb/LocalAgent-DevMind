import requests
from bs4 import BeautifulSoup

def fetch_top_stories(url):
    """Extrae los titulares de una página de noticias."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Buscamos etiquetas h2 que suelen ser titulares
        headlines = [h.get_text() for h in soup.find_all('h2')[:5]]
        return headlines
    except Exception as e:
        return f"Error en la conexión: {e}"

if __name__ == "__main__":
    site = "https://news.ycombinator.com"
    stories = fetch_top_stories(site)
    print(f"Top stories from {site}:", stories)
