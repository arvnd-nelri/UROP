import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

def downloadimg(name):
    query = name+" logo"
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    img_tag = soup.find("img", {"class": "yWs4tf"})
    print(img_tag)
    if img_tag is not None:
        img_link = img_tag.get("src")
        print(img_link)
        response = requests.get(img_link)
        image_bytes = BytesIO(response.content)
        img = Image.open(image_bytes)
        img.save(f"F:\APSSDC\CoupSwap_Project\static\images\companies\{name}.png")
        print("image downloaded")
    else:
        print("No image found on the page.")
