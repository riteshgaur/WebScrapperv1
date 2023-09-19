# import os
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin, urlparse

# # Define the URL of the website you want to scrape
# base_url = "https://www.villeroy-boch.cn/cn/home.html"  # Replace with your target website URL

# # Define the directory where you want to save the content
# output_directory = "website_content"

# # Create the output directory if it doesn't exist
# os.makedirs(output_directory, exist_ok=True)

# # Function to download and save an image or video
# def download_media(media_url, save_path):
#     response = requests.get(media_url)
#     with open(save_path, "wb") as file:
#         file.write(response.content)

# # Function to scrape a webpage and save its content
# def scrape_page(url, page_dir):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
    
#     # Create a subdirectory for this page
#     os.makedirs(page_dir, exist_ok=True)
    
#     # Download and save images and videos
#     media_tags = soup.find_all(["img", "video"])
#     for media_tag in media_tags:
#         media_url = urljoin(url, media_tag["src"])
#         media_name = os.path.basename(urlparse(media_url).path)
#         media_save_path = os.path.join(page_dir, media_name)
#         download_media(media_url, media_save_path)
    
#     # Save the text content (e.g., HTML, text)
#     with open(os.path.join(page_dir, "page_content.html"), "w", encoding="utf-8") as file:
#         file.write(soup.prettify())

# # Function to recursively scrape the website
# def scrape_website(url, current_dir):
#     scrape_page(url, current_dir)
    
#     # Find links to sub-pages
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     sub_page_links = soup.find_all("a", href=True)
    
#     for link in sub_page_links:
#         sub_page_url = urljoin(url, link["href"])
#         sub_page_name = os.path.basename(urlparse(sub_page_url).path)
#         sub_page_dir = os.path.join(current_dir, sub_page_name)
#         scrape_website(sub_page_url, sub_page_dir)

# # Main function
# def main():
#     # Create a directory for the website content
#     os.makedirs(output_directory, exist_ok=True)
    
#     # Start scraping the website from the base URL
#     scrape_website(base_url, output_directory)

# if __name__ == "__main__":
#     main()





#-----Working code------

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Define the URL of the website you want to scrape
base_url = "https://pro.villeroy-boch.com/picdb/produkte/"  # Replace with your target website URL

# Define the directory where you want to save the content
output_directory = "website_content"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Function to download and save an image or video
def download_media(media_url, save_path):
    response = requests.get(media_url)
    with open(save_path, "wb") as file:
        file.write(response.content)

# Function to scrape a webpage and save its content
def scrape_page(url, page_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Create a subdirectory for this page
    os.makedirs(page_dir, exist_ok=True)
    
    # Download and save images and videos
    media_tags = soup.find_all(["img", "video"])
    for media_tag in media_tags:
        media_url = urljoin(url, media_tag["src"])
        media_name = os.path.basename(urlparse(media_url).path)
        media_save_path = os.path.join(page_dir, media_name)
        download_media(media_url, media_save_path)
    
    # Save the text content (e.g., HTML, text)
    with open(os.path.join(page_dir, "page_content.html"), "w", encoding="utf-8") as file:
        file.write(soup.prettify())

# Main function
def main():
    # Create a directory for the website content
    os.makedirs(output_directory, exist_ok=True)
    
    # Get the initial page of the website
    initial_page_url = base_url  # You can modify this to start from a specific page
    scrape_page(initial_page_url, output_directory)

if __name__ == "__main__":
    main()
