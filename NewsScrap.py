import requests
import pandas as pd

def fetch_news(api_key, query):
    url = f"https://newsapi.org/v2/everything?q={query} cyber fraud India&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['articles']

def extract_scam_amount(article):
    content = article.get('content', '')
    amount = 0
    if content:
        # Example regex pattern for extracting currency amounts (e.g., $10,000)
        import re
        pattern = r'\$?(\d{1,3}(,\d{3})*(\.\d+)?)'  # Modify this pattern according to the format in the articles
        amounts = re.findall(pattern, content)
        if amounts:
            amount += sum(float(x[0].replace(',', '')) for x in amounts)
    return amount

def main():
    api_key = '9c01e7858104457aabdc00bd57160faa'  # Replace 'YOUR_NEWS_API_KEY' with your News API key
    query = "cyber fraud india"  # Modify the query as per your requirement
    output_file = 'cyber_fraud_news_with_amount.xlsx'  # Output Excel file name

    news_articles = fetch_news(api_key, query)
    total_scam_amount = sum(extract_scam_amount(article) for article in news_articles)

    print("Total scammed amount:", total_scam_amount)

    # Write to Excel
    df = pd.DataFrame([[article['title'], article['url']] for article in news_articles], columns=['Title', 'URL'])
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    main()
