# Make sure to install these libraries using pip if you haven't already:
# pip install requests beautifulsoup4


import re
import requests
from bs4 import BeautifulSoup

def extract_social_links(soup):
    social_links = []
    social_patterns = ['facebook.com',  'linkedin.com']
    
    for a_tag in soup.find_all('a', href=True):
        for pattern in social_patterns:
            if pattern in a_tag['href']:
                social_links.append(a_tag['href'])
    
    return social_links

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.findall(email_pattern, text, re.IGNORECASE)

def extract_phone_numbers(text):
    phone_pattern = r'(?<!\d)(?:(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})(?!\d)'
    return re.findall(phone_pattern, text)

# Get user input for the website URL
website_url = input("Enter the website URL: ")

# Send a request to the website and retrieve its content
response = requests.get(website_url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract social links
social_links = extract_social_links(soup)
print("Social Links:")
for link in social_links:
    print(link)

# Extract emails
emails = extract_emails(html_content)
print("\nEmail Addresses:")
for email in emails:
    print(email)

# Extract phone numbers
phone_numbers = extract_phone_numbers(html_content)
print("\nPhone Numbers:")
for number in phone_numbers:
    print(number)

