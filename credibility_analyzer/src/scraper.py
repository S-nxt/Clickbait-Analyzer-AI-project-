import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    """
    Extracts article title and paragraph body from a live URL.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Grab title
        title = soup.find('h1')
        title_text = title.get_text().strip() if title else ""
        
        # Grab body paragraphs
        paragraphs = soup.find_all('p')
        body_text = " ".join([p.get_text().strip() for p in paragraphs])
        
        full_article = f"{title_text} {body_text}"
        
        if len(full_article.strip()) < 50:
            return None, "Article text too short or blocked by site."
            
        return full_article, None

    except Exception as e:
        return None, f"Scraping Error: {str(e)}"

# Quick standalone test
if __name__ == "__main__":
    test_url = "https://www.bbc.com/news"
    text, error = scrape_article(test_url)
    if error:
        print("Error:", error)
    else:
        print("Scraped Text Preview:", text[:300])