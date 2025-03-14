import requests

def fetch_image_from_lexica(style):
    lexica_url = f"https://lexica.art/api/search?q={style}"
    response = requests.get(lexica_url)
    
    if response.status_code == 200:
        data = response.json()
        if "images" in data and len(data["images"]) > 0:
            return data["images"][0]["src"]
    
    return None  # Return None if no images are found