import requests, json

# security_code = input("Enter the security code:")
# page_wanted = input("How many page you want:")
merged = []

# def getJsonByPage(page_wanted):
#     # 按页获取数据并保存为json文件
#     #TODO: 1.自定义号码以及页数
#     #      2.不生成json临时文件
#     #      3.改为with open

#     for i in range(1,531):
        # endPage = i * 10
        # beginPage = endPage - 9
        # url = f"http://ipo.sseinfo.com/info/ipoInfoDisplay/searchIPOInquiryList.do?&isPagination=true&securityCode=688586&pageHelp.beginPage={beginPage}&pageHelp.endPage={endPage}"
        # filName = f"page_{i}.json"
        # # print(filName)
        # r = requests.get(url)
        # r = r.content.decode('utf-8')
        # f = open(filName, mode = 'w',encoding='utf-8')
        # f.write(r)
        # f.close
        # print(f"Page {i} has been saved.")

def getOriginData(page_no):
    # 提取JSON中的原始数据
    data = json.load(open(f'./json/page_{page_no}.json','r',encoding="utf-8"))["result"]
    print(type(data))
    return data

def dataMerger(pagetomerge):
    # 将数据合并到主表中
    merged.extend(pagetomerge)
    return merged

def converToCsv():
    pass

for i in range(1,531):
    jsonfile = json.load(open(f'./json/page_{i}.json','r',encoding="utf-8"))["result"]
    dataMerger(jsonfile)



with open('data.json', 'w', encoding="utf-8" ) as f:
    f.write(str(merged))


