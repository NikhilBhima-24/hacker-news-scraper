import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_hacker_news():
    print("Initiating web scraper for Hacker News...")
    url = 'https://news.ycombinator.com/'
    
    try:
        # Add a standard user-agent to prevent the request from being blocked
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all article rows
        articles = soup.find_all('tr', class_='athing')
        
        scraped_data = []
        
        for article in articles[:15]: # Scrape the top 15 articles
            title_tag = article.find('span', class_='titleline')
            if title_tag and title_tag.a:
                title = title_tag.a.text
                link = title_tag.a.get('href')
                scraped_data.append([title, link])
                
        return scraped_data

    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return []

def save_to_csv(data):
    if not data:
        print("No data to save.")
        return
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"tech_news_{timestamp}.csv"
    
    print(f"Saving {len(data)} articles to {filename}...")
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Article Title', 'URL']) # Write header
        writer.writerows(data)
        
    print("Data export complete!")

def main():
    data = scrape_hacker_news()
    save_to_csv(data)

if __name__ == "__main__":
    main()
