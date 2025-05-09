import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_data = []

# 定義需要的欄位
target_columns = [
    "許可證號碼", "許可證號碼_連結",
    "普通名稱", "普通名稱_連結",
    "廠牌名稱",
    "劑型",
    "含量",
    "Under Permit",
    "混合",
    "廠商名稱", "廠商名稱_連結",
    "國外原製造廠", "國外原製造廠_連結",
    "有效日期",
    "標示_連結",
    "條碼_連結",
    "使用範圍_連結",
]

for page in range(1, 65):
    print(f"📄 正在抓第 {page} 頁")
    url = f"https://pesticide.aphia.gov.tw/information/Query/RegisterList/?type=1&page={page}&pagesize=100"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select("div.table-data-list tbody tr")

    for row in rows:
        tds = row.find_all("td")
        if len(tds) < 10:  # 基本欄位檢查
            print(f"⛔ 欄位不足 (只有 {len(tds)} 個)，跳過")
            continue

        # 取得原始欄位文字與超連結
        def get_text_and_link(td):
            text = td.get_text(strip=True)  # 取得純文字並去除空白
            a_tag = td.find("a")  # 檢查是否有超連結(包在內)
            href = a_tag["href"] if a_tag and a_tag.get("href") else ""
            full_url = f"https://pesticide.aphia.gov.tw{href}" if href.startswith("/") else ""
            return text, full_url

        # 處理許可證號碼 (拆分為類型和號碼)
        permit_text, permit_link = get_text_and_link(tds[0])
        permit_parts = permit_text.strip().split()
        if len(permit_parts) >= 2:
            permit_type = permit_parts[0]
            permit_number = permit_parts[-1]
        else:
            permit_type = permit_text
            permit_number = ""

        row_data = {
            "許可證類型": permit_type,
            "許可證號碼": permit_number,
            "許可證號碼_連結": permit_link,
            "普通名稱": get_text_and_link(tds[1])[0],
            "普通名稱_連結": get_text_and_link(tds[1])[1],
            "廠牌名稱": get_text_and_link(tds[2])[0],
            "劑型": get_text_and_link(tds[3])[0],
            "含量": get_text_and_link(tds[4])[0],
            "Under Permit": get_text_and_link(tds[5])[0],
            "混合": get_text_and_link(tds[6])[0],
            "廠商名稱": get_text_and_link(tds[7])[0],
            "廠商名稱_連結": get_text_and_link(tds[7])[1],
            "國外原製造廠": get_text_and_link(tds[8])[0],
            "國外原製造廠_連結": get_text_and_link(tds[8])[1],
            "有效日期": get_text_and_link(tds[9])[0],
            "標示_連結": get_text_and_link(tds[11])[1] if len(tds) > 11 else "",
            "條碼_連結": get_text_and_link(tds[12])[1] if len(tds) > 12 else "",
            "使用範圍_連結": get_text_and_link(tds[13])[1] if len(tds) > 13 else "",
        }

        all_data.append(row_data)
        print("✅ 加入一筆資料")
    time.sleep(0.5)

# 建立DataFrame並只保留需要的欄位
final_columns = [
    "許可證類型", "許可證號碼", "許可證號碼_連結",
    "普通名稱", "普通名稱_連結",
    "廠牌名稱",
    "劑型",
    "含量",
    "Under Permit",
    "混合",
    "廠商名稱", "廠商名稱_連結",
    "國外原製造廠", "國外原製造廠_連結",
    "有效日期",
    "標示_連結",
    "條碼_連結",
    "使用範圍_連結",
]

df = pd.DataFrame(all_data)[final_columns]
df.to_csv("taiwan_pesticides_cleaned.csv", index=False, encoding="utf-8-sig")
print(f"✅ 完成，共抓到 {len(df)} 筆資料，欄位已清理並命名")