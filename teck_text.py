# 用Python自動抓取文章練閱讀（範例）
import requests
from bs4 import BeautifulSoup
url = "https://www.theguardian.com/technology"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
headlines = [h3.text for h3 in soup.find_all('h3')[:5]]
print("今日科技頭條:", headlines)