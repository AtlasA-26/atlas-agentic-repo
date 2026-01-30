import feedparser
import pandas as pd
import os
from datetime import datetime

# Real African-Centric RSS Feeds
SOURCES = {
    "AJOL Africa": "https://www.ajol.info/index.php/index/rss",
    "PAMJ": "https://www.panafrican-med-journal.com/rss/pamj.xml",
    "PubMed Biotech": "https://pubmed.ncbi.nlm.nih.gov/rss/search/1M_D0Zf..."
}

def run_scrape():
    results = []
    for name, url in SOURCES.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            # Simple regional tagging
            region = "Africa" if "africa" in entry.title.lower() or "ajol" in name.lower() else "Global"
            results.append({
                "Date": datetime.now().strftime("%Y-%m-%d"),
                "Source": name,
                "Region": region,
                "Headline": entry.title,
                "Link": entry.link
            })
    
    df = pd.DataFrame(results)
    
    # CRITICAL: Create directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/research_data.csv", index=False)
    print("Scrape successful. CSV saved.")

if __name__ == "__main__":
    run_scrape()