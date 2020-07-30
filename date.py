import requests, json, csv


url = "http://ipo.sseinfo.com/info/commonQuery.do?jsonCallBack=jsonpCallback72297427&sqlId=COMMON_SSE_IPO_PROCESS_DETAILS_STATUS_C&securityCode=688589&_=1596083229452"
merged = []

# r = requests.get(url)
# r = r.content.decode('utf-8')
# with open(f'./date/1.json','w',encoding = "utf-8") as f:
#             f.write(r)
# print(r)

# f = open('scode.csv', 'r', encoding='utf-8-sig')
# csvreader = csv.reader(f)
# security_codes = list(csvreader)
# # print(security_codes)
# # security_code = 688200
security_codes = ['688589', '688189', '688200', '688228', '688233', '688169', '601778', '688568', '600956', '688229', '601456', '605188', '688335', '688090', '603949', '688004', '688379', '605388', '603931', '688981', '603948', '688580', '605118', '688256', '688106', '605158', '688339', '688365', '688500', '688488', '688065', '605100', '688505', '605088', '600918', '605222', '601696', '688096', '688060', '688555', '688508', '688579', '688069', '603195', '605366', '603893', '688561', '688520', '688338', '688588', '605399', '688398', '605199', '688312', '688598', '688336', '688396', '688126', '603095', '603290', '688466', '688278', '688599', '605108', '603353', '688518', '688186', '688155', '688556', '688558', '605288', '605166', '688080', '688286', '688157', '688519', '688516', '688165', '688055', '601827', '688085', '688566', '688277', '688528', '603682', '603392', '688050', '688567', '603950', '688313', '605066', '605333', '603719', '603087', '688521', '601609', '688311', '605318', '603408', '688208', '688077', '605001', '688051', '688222', '688418', '688027']
# security_codes = ['688589']
def getDatesData(security_code):
        url = f"http://ipo.sseinfo.com/info/commonQuery.do?jsonCallBack=jsonpCallback&sqlId=COMMON_SSE_IPO_PROCESS_DETAILS_STATUS_C&securityCode={security_code}"
        fileName = f"{security_code}.json"
        r = requests.get(url)
        r = r.content.decode('utf-8').lstrip('jsonpCallback(').rstrip(')')
        with open(f'./date/{fileName}','w',encoding = "utf-8") as f:
            f.write(r)
        print(f"{security_code} has been saved.")

def getOriginData(page_no):
    # 提取JSON中的原始数据
    data = json.load(open(f'./date/{security_code}.json','r',encoding="utf-8"))["result"]
    return data

def dataMerger(pagetomerge):
    # 将数据合并到主表中
    merged.extend(pagetomerge)
    return merged


# for security_code in security_codes:
#     getDatesData(security_code)
    


for security_code in security_codes:
    jsonfile = json.load(open(f'./date/{security_code}.json','r',encoding="utf-8"))["result"]
    dataMerger(jsonfile)

# 把列表转为格式化为Json形式的字符串
output = json.dumps(merged, ensure_ascii=False)

with open('date.json', 'w', encoding="utf-8" ) as f:
    f.write(output)

