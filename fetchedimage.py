import requests 
import os
from urllib.parse import urlparse
from PIL import Image

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

# Get URL from user
    url = input("Please enter the image URL: ")


# Create the fetched_images folder if it doesn't exist
    try:
        folder = "fetched_images"
        os.makedirs(folder, exist_ok=True)

    # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raise exception for bad status codes

# Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename =os.path.basename(parsed_url.path)
    
        if not filename:
            filename = "fetchedimage.jpg"
    
# Save the image
        filepath = os.path.join(folder, filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"Successfully fetched: {filename}")
        print(f"Image saved to {filepath}")
        print("\nConnection Strengthened. Community enriched.")

# Open and display the image

        img = Image.open(filepath)
        img.show()

    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
    
# Open and display the image

    img = Image.open(filepath)
    img.show()

# Run the program
if __name__ == "__main__":
    main()
    

