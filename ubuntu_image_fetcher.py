import os
import requests
from urllib.parse import urlparse, unquote
import datetime

def download_image():
    url = input("Enter the direct image URL: ").strip()
    if not url:
        print("Error: No URL provided.")
        return
    
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        if not response.headers.get('content-type', '').startswith('image/'):
            print("Error: The provided link is not an image.")
            return
        
        os.makedirs("Fetched_Images", exist_ok=True)
        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(8192):
                file.write(chunk)
        
        print(f"✅ Success! Saved as '{filename}' in Fetched_Images/")
        
    except Exception as e:
        print(f"❌ Download failed: {e}")

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    if path and '.' in path:
        base = path.split('/')[-1].split('.')[0]  # remove extension
        return f"{base}.jpg"  # always save as .jpg
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"image_{timestamp}.jpg"

if __name__ == "__main__":
    download_image()
