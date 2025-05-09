import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_data = []

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
        cols = []
        for td in row.find_all("td"):
            text = td.get_text(strip=True)
            link = td.find("a")
            href = link["href"] if link and link.get("href") else ""
            full_url = f"https://pesticide.aphia.gov.tw{href}" if href.startswith("/") else href
            cols.extend([text, full_url])
        all_data.append(cols)

    time.sleep(0.5)

# 加入欄位名稱
columns = [
    "許可證號碼", "許可證號碼_連結",
    "普通名稱", "普通名稱_連結",
    "廠牌名稱", "廠牌名稱_連結",
    "劑型", "劑型_連結",
    "含量", "含量_連結",
    "Under Permit", "Under Permit_連結",
    "混合", "混合_連結",
    "廠商名稱", "廠商名稱_連結",
    "國外原製造廠", "國外原製造廠_連結",
    "有效日期", "有效日期_連結",
    "備註", "備註_連結",
    "標示", "標示_連結",
    "條碼", "條碼_連結",
    "使用範圍", "使用範圍_連結",
]

df = pd.DataFrame(all_data, columns=columns)
df.to_csv("taiwan_pesticides_with_links_named.csv", index=False, encoding="utf-8-sig")
print(f"✅ 完成，共抓到 {len(df)} 筆資料，欄位已命名")
