import requests, json

security_code = input("Enter the security code:")
page_wanted = int(input("How many page you want:")) + 1
merged = []

def getJsonByPage(page_wanted):
#     # 按页获取数据并保存为json文件
#     #TODO: 1.不生成json临时文件
    for page_no in range(1,page_wanted):
        endPage = page_no * 10
        beginPage = endPage - 9
        url = f"http://ipo.sseinfo.com/info/ipoInfoDisplay/searchIPOInquiryList.do?&isPagination=true&securityCode=688586&pageHelp.beginPage={beginPage}&pageHelp.endPage={endPage}"
        fileName = f"page_{page_no}.json"
        r = requests.get(url)
        r = r.content.decode('utf-8')
        # f = open(filName, mode = 'w',encoding='utf-8')
        # f.write(r)
        # f.close
        with open(f'./json/{fileName}','w',encoding = "utf-8") as f:
            f.write(r)
        print(f"Page {page_no} has been saved.")

def getOriginData(page_no):
    # 提取JSON中的原始数据
    data = json.load(open(f'./json/page_{page_no}.json','r',encoding="utf-8"))["result"]
    return data

def dataMerger(pagetomerge):
    # 将数据合并到主表中
    merged.extend(pagetomerge)
    return merged

def converToCsv():
    pass

getJsonByPage(page_wanted)


for i in range(1,page_wanted):
    jsonfile = json.load(open(f'./json/page_{i}.json','r',encoding="utf-8"))["result"]
    dataMerger(jsonfile)

# 把列表转为格式化为Json形式的字符串
output = json.dumps(merged, ensure_ascii=False)

with open('data.json', 'w', encoding="utf-8" ) as f:
    f.write(output)