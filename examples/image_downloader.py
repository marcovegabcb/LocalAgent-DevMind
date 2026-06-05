import requests
from PIL import Image
from io import BytesIO

def download_and_show_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    print(f"Imagen descargada: {img.size} - {img.mode}")
    return img

img = download_and_show_image("https://via.placeholder.com/150")
print("Tamaño:", img.size)
