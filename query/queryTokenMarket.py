# coding=utf-8
import re

import time
import urllib.request

from query.IcoData import IcoData
from query.enum.TypeEnum import TypeEnum
from urllib.request import Request, urlopen


resultSet = set([])
originSet = set([])

def gethtml():
    req = Request(
        'http://tokenmarket.net/ico-calendar',
        headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    return webpage.decode('utf-8')

def getHtml():
    responseCode = 0
    count = 0
    while responseCode != 200 and count < 3:
        count += 1
        # 网址
        url = "https://tokenmarket.net/ico-calendar"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.63 Safari/537.36'}
        # 请求
        request = urllib.request.Request(url=url, headers=headers)

        # 爬取结果
        response = urllib.request.urlopen(request)

        data = response.read()
        print( data)
        # 设置解码方式
        data = data.decode('utf-8')
        if (response.getcode() == 200):
            return data

    return None



def parase(data):
    length = len(data)
    if length < 3:
        raise Exception("数据解析错误", data)
    if (data[1].find("closes") > 0):
        icodata = IcoData(TypeEnum.past, data[0].strip(), data[2].strip(), None)
    elif (data[1].find("opens") > 0):
        icodata = IcoData(TypeEnum.upcoming, data[0].strip(), data[2].strip(), None)
    elif (data[1].find("text") > 0):
        icodata = IcoData(TypeEnum.onGoing, data[0].strip(), paraseText(data[1]), data[2].strip())
    print (icodata)


def paraseText(text):
    text = text.strip()
    pattern = re.compile('<p>(.*?)</p>.*?<p>.*?</p>', re.S)
    text = re.findall(pattern, text)
    text = text.pop().strip()
    return text


def readFile():
    file = open("icoText.txt", 'r',encoding='latin1')
    text = file.read()
    handleoriginText(text)
    return list(resultSet)


def handleoriginText(text):
    # pattern = re.compile(
    #     '<tr>.*?<td.*?class="col-asset-name.*?>.*?<a.*?>(.*?)</a>.*?</td>.*?<td>(.*?)</td>.*?<td.*?>.*?<p>(.*?)</p>.*?</td>.*?</td>.*?</tr>',
    #     re.S)
    global resultSet
    global originSet
    pattern = re.compile(
        '<td.*?class="col-asset-name.*?>.*?<a.? href=.*?>(.*?)</a>.*?</td>',
        re.S)
    items = re.findall(pattern, text)
    resultSet.clear()
    for item in items:
        itemStr = item.strip()
        if(itemStr not in originSet):
            originSet.add(itemStr)
            resultSet.add(itemStr)
    return resultSet



def getFromTokenMarket():
    data = gethtml()
    if(data != None):
        handleoriginText(data)
        return list(resultSet)
    else:
        raise Exception("从tokenMarket获取数据出错")


def dateParse():
    date ="10. Aug 2017"
    res =time.strptime(date,"%d. %b %Y")
    print (time.mktime(res))

# getFromTokenMarket()
# dateParse()
gethtml()