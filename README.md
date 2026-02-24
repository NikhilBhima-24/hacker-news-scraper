# Tech News Web Scraper

An automated Python utility built to scrape real-time data from Hacker News (news.ycombinator.com). This project demonstrates the fundamentals of web scraping, HTML DOM parsing, and automated data exporting using Python.

## Features
* **DOM Parsing:** Utilizes `BeautifulSoup` to navigate and extract specific HTML elements (titles and links) from a live webpage.
* **HTTP Requests:** Implements the `requests` library with custom User-Agent headers to reliably fetch web page content.
* **Automated Data Export:** Dynamically generates a timestamped CSV file (`tech_news_YYYYMMDD_HHMMSS.csv`) containing the scraped data for easy analysis.
* **Error Handling:** Includes basic try-except blocks to gracefully handle HTTP request failures or parsing errors.

## Tech Stack
* **Python 3.x**
* **BeautifulSoup4** (HTML Parsing)
* **Requests** (HTTP Client)
* **CSV** (Native Python Data Export)

## Installation & Setup

1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/NikhilBhima-24/hacker-news-scraper.git](https://github.com/NikhilBhima-24/hacker-news-scraper.git)
   cd hacker-news-scraper
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script directly from your terminal. It will fetch the top 15 trending articles from Hacker News and automatically generate a CSV file in the same directory.

```bash
python scraper.py
```

### Sample Output (CSV)
| Article Title | URL |
|---|---|
| Show HN: A new way to visualize data | https://example.com/data |
| The history of the Python GIL | https://example.com/python |
