import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_data = []

# 頁數：1～64
for page in range(1, 65):
    print(f"📄 正在抓第 {page} 頁")
    url = f"https://pesticide.aphia.gov.tw/information/Query/RegisterList/?type=1&page={page}&pagesize=100"

    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select("div.table-data-list tbody tr")

    for row in rows:
        cols = [td.get_text(strip=True) for td in row.find_all("td")]
        all_data.append(cols)

    time.sleep(0.5)  # 加一點延遲避免太快被封鎖

# 存成 DataFrame
df = pd.DataFrame(all_data)
df.to_csv("taiwan_pesticides_full.csv", index=False, encoding="utf-8-sig")
print(f"✅ 完成，共抓到 {len(df)} 筆資料")
