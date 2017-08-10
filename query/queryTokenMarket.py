import urllib.request
from bs4 import BeautifulSoup
# 网址
url = "https://tokenmarket.net/ico-calendar"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}
# 请求
request = urllib.request.Request(url=url,headers=headers)

# 爬取结果
response = urllib.request.urlopen(request)

data = response.read()

# 设置解码方式
data = data.decode('utf-8')

# 打印结果
# print(data)
soup = BeautifulSoup(data,"html.parser")
# print(soup.find_all("td",class_="col-asset-name"))
# print(soup.find_all("tbody"))
# print("-----------------------------------------------------------")
print(soup.find_all("tbody").__sizeof__())
for singleSoup in soup.find_all("tbody"):
    print(singleSoup)
    print("---------------------------------------------")
    print(singleSoup.td.p)
    print("---------------------------------------------")
# 打印爬取网页的各类信息

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())

# def parase(data):
#     soup = BeautifulSoup(data)
#     print(soup)