"""
import requests  # 匯入 requests 套件
from urllib.parse import urljoin  # 匯入用來解析及組合網址的函式


url = "https://4-learn.github.io/crawler-playground/v1/api/laws/N0030001/page-1.json" # 設定第一頁的 API 網址


session = requests.Session() # 建立 Session，共用設定並盡可能重複利用連線


articles = [] # 建立空列表，準備儲存所有頁面的條文


while url: # 只要 url 為真值，就繼續執行迴圈

    r = session.get(url, timeout=10) # 向目前 url 發送 GET 請求，將 Response 物件存入 r
    session.headers["User-Agent"] = "my-python-crawler/1.0"
    r.raise_for_status()    # 檢查 HTTP 回應是否有 4xx、5xx 錯誤

    data = r.json()  # 將回傳的 JSON 解析為 Python 資料結構
    

    
    articles.extend(data["articles"]) # 把目前頁面的所有條文加入 articles 列表

    
    print("目前頁數：", data["page"]) # 印出目前抓取的頁數

    
    if data["next"]: # 如果 API 提供下一頁網址

        
        url = urljoin(url, data["next"]) # 組合下一頁完整網址並更新 url

    else: # 沒有下一頁，設定為 None，讓 while 停止
        
        url = None

print("全部下載完成")
print("總條數：", len(articles))

assert len(articles) == data["total"]
assert len(articles) == 98

for law in data["laws"]:
    if law["name"] == "職業安全衛生法":
        pcode = law["pcode"]
        break

print(pcode)
"""



data = {
    "laws": [
        {"name": "勞動基準法", "pcode": "N0030001"},
        {"name": "職業安全衛生法", "pcode": "N0060001"},
        {"name": "就業服務法", "pcode": "N0090001"}
    ]
}



for law in data["laws"]:
    if law["name"] == "職業安全衛生法":
        pcode = law["pcode"]
        break

print(pcode)
  
