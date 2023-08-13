import requests
from bs4 import BeautifulSoup

# Prompt the user to input the URL
url = input("Enter the URL you want to scrape: ")

# Get the filename for the output text file
output_file = "output.txt"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all("a")

with open(output_file, "w") as f:
    for link in links:
        href = link.get("href")
        if href:
            # Get the plain text content of the link and remove leading/trailing spaces
            text_content = link.get_text(strip=True)
            f.write(text_content + "\n")

print("Text content saved to", output_file)
