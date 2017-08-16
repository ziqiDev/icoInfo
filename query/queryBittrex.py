import datetime
import urllib.request
import json
import time


def queryBittrexData():
    url2 = "https://bittrex.com/api/v1.1/public/getmarkets"
    data = urllib.request.urlopen(url2).read()
    z_data = data.decode('UTF-8')
    json_Str = json.loads(z_data)
    jsonList = json_Str["result"]
    resList = []
    currentTime = getYesterday()
    for singleCoin in jsonList:
        created = singleCoin["Created"]
        index = created.find(".")
        created = created[:index]
        createdTime = time.mktime(time.strptime(created, '%Y-%m-%dT%H:%M:%S'))
        if (createdTime > currentTime):
            resList.append(singleCoin["MarketName"])

def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return time.mktime(time.strptime(yesterday.strftime('%Y-%m-%d'), '%Y-%m-%d'))


queryBittrexData()
# getTimeOClockOfToday()
# getTimeOClockOfToday()
