import pandas as pd
"""
為了顯示的漂亮, 
1. 我刻意的把印出來的row 和column 只顯示六個
2. 設定每一個格子最大的列印字數
"""
# pd.set_option('display.max_rows', 10)
# pd.set_option('display.max_columns', 4)
pd.options.display.max_colwidth = 20

df = pd.read_csv("../ted_main.csv", encoding ="utf-8")

#DataFrame 大小
#print(df.shape)
"""
#你必須把想要的標籤集合成一個list 傳入行操作的[ ]，所以這裡兩個[ ] 代表截然不同的意思
1. 外面的[ ]: DataFrame 的行操作2. 裡面的[ ]: 把標籤集合起來的list
"""
# print(df[["comments", "description", "url"]])

"""
1. 篩選列的時候，我們使用的是.loc(少用, 如果有自己創造列標籤才用得上)，iloc(常用, 使用
pandas 幫你創的0 開始的列標籤)
2. 使用iloc 的時候會得到一個像是list 的資料，接著就可以使用類似list 的操作來操作
3. .iloc -> [“第一筆資料”, “第二筆資料”, “第三筆資料”, …, “最後一筆資料”]
    單列篩選在.iloc 這個列表加上[ 座號]
    多列篩選 .iloc 後使用[頭部座號(包括): 尾部座號(不包括)]
    頭幾列篩選andas 也提供一些讓你偷懶的函式，如果是要篩選頭幾列的話用head 函式來篩選
    尾幾列篩選 使用tail 函式來做尾部的篩選
"""
#print(df.iloc[0:5])
#print(df.head(5))
#print(df.tail(5))
"""
表格行＋列篩選
    1. 只要是DataFrame 就可以使用上面的行或者列篩選
    2. 所以你可以任意組合行列篩選，先[] 再.iloc[]，或者先.iloc[] 再[]
列過濾
    1. 過濾操作是把符合我們期待的列留下來，不符合期待的列丟掉的一個操作
    2. 核心概念是做一個跟我們的資料筆數一樣大的布林list，對到True 的資料留下，對到False
        的資料丟掉
    3. (特別) 這時候一樣是對你的DataFrame 加上[ ] , 把布林list 丟進你的[ ] 裡
        # 只取三列資料
        # 過濾, 創一個三個大小的True, False list
          對到True(第一三筆) 留下, 對到False(第二筆) 丟掉
"""
#print(df[ ["comments", "description", "duration"] ].iloc[ :5 ])
#test = df.iloc[:3]
#print(test[ [True, False, True] ])



"""藉由pandas 定義的contains 對裡面每個元素做出布林判斷"""
bool_filter = df["description"].str.contains("Sir")
#print(bool_filter)
"""帶入DataFrame"""
#print(df[bool_filter])
"""
你仔細對照, 你會發現contains 是只要有contains 那個字串就可以
並不一定是完整的一個字(Sirena 也算有contains Sir)
但我們可以使用格式(正規表示式) 來結合contains
記得在你格式字串前加上r(不轉換任何東西, 原始字串)
不然\b 會被當成backspace, 而不是兩個字
"""
#print(df[ df["description"].str.contains(r"\bSir\b") ])



"""
to_csv 重要參數
1. 必要參數: 檔案位置
2. 選用參數encoding(有預設值): 讀取使用編碼
3. 選用參數index(有預設值True): 要不要把pandas 幫你產生的列編號寫進檔案, True: 寫,
False: 不寫, 通常我會選False
# 用剛剛的filter 過後的東西做個例子
# 儲存成csv
# 把剛剛儲存的東西讀出來給你看看
"""
#filter_df = df[ df["description"].str.contains(r"\bSir\b") ]
#filter_df.to_csv("filter.csv", encoding = "utf-8", index = False)
#df2 = pd.read_csv("filter.csv", encoding = "utf-8")
#print(df2)



"""
你可以使用drop 來刪除多行，不過記得如果你想要讓df 變成刪除過後的樣子要記得設定回去
刪除多行, axis = 1 指的是刪除行的意思, axis = 0 是刪除列的意思
"""
#print( df.drop(["url", "views"], axis = 1))
"""
轉換類別
apply 是一個最重要的可以幫你轉換一行裡面所有格子的方便函式，大家在學習Pandas 的時
候一定要好好學會apply 的使用方式，我們發現我們在TED 資料集裡看到的時間都是一些奇怪形
式，譬如這樣，這是什麼呢？
"""
#print(df["film_date"])

"""這叫做UNIX 時間或者POSIX 時間，是從1970 年1 月1 日0 時0 分0 秒起至現在的總秒數，
也是電腦常常使用的時間，我們可以輕易的把它轉換成我們熟悉的西元時間，這裡我們使用內建的
datetime 模組來轉換
# 在使用apply 前, 我們要定義一個流程
# 接著就可以把這流程對每一個格子做一次
# 這裡要記得, python 在print 的時候會先做一次str 的轉換
# 所以我們要做一次str 轉換
# 不用帶入data, apply 會自動幫你把每個格子裡的資料帶入
"""
from datetime import datetime
#import pytz
#print("原始:", df["film_date"][0])
#print("轉換(當地時間):", datetime.fromtimestamp(df["film_date"][0]))
def timeflow(data):
    return str(datetime.fromtimestamp(data))
#print(df["film_date"].apply(timeflow))
"""設定回去原表格"""
df["film_date(datetime)"] = df["film_date"].apply(timeflow)
print(df[ ["film_date", "film_date(datetime)"] ])