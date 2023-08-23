import requests
from bs4 import BeautifulSoup
import re

# List of technologies and their corresponding regex patterns
technologies = {
    "jQuery": r"(?i)jquery[\s\S]*?(\d+\.\d+\.\d+)",
    "React.js": r"(?i)react[\s\S]*?(\d+\.\d+\.\d+)",
    "WooCommerce": r"(?i)woocommerce",
    "Bootstrap": r"(?i)bootstrap[\s\S]*?(\d+\.\d+\.\d+)",
    "Shopify": r"(?i)(\b\w+\.)?myshopify\.com",
    "Next.js": r"(?i)next[\s\S]*?(\d+\.\d+\.\d+)",
    "Materialize CSS": r"(?i)materialize[\s\S]*?(\d+\.\d+\.\d+)",
    "PHP": r"(?i)php[\s\S]*?(\d+\.\d+\.\d+)",
    "Python": r"(?i)python[\s\S]*?(\d+\.\d+\.\d+)",
    "Google Maps": r"^https?\:\/\/(www\.|maps\.)?google\.[a-z]+\/maps\/?\?([^&]+&)*(ll=-?[0-9]{1,2}\.[0-9]+,-?[0-9]{1,2}\.[0-9]+|q=[^&]+)+($|&)",
    
}

# Sample website where you can find
sample_website = input("Enter the Website link")

response = requests.get(sample_website)
if response.status_code != 200:
    print("Failed to fetch the webpage.")
else:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    print("Technologies detected:")
    for tech, pattern in technologies.items():
        found = False
        for script in soup.find_all("script"):
            if re.search(pattern, str(script), re.IGNORECASE):
                version = re.search(pattern, str(script), re.IGNORECASE).group(1)
                print(f"{tech} (Version: {version})")
                found = True
                break
        if not found:
            for tag in soup.find_all(True):
                if re.search(pattern, str(tag), re.IGNORECASE):
                    print(tech)
                    break