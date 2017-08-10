import urllib.request
import json
import time


def getdata():
    url2 ="https://bittrex.com/api/v1.1/public/getmarkets"
    data = urllib.request.urlopen(url2).read()
    z_data = data.decode('UTF-8')
    print(z_data)
    json_Str = json.loads(z_data)
    print(json_Str["result"])
    print(type(json_Str["result"]))
    print (time.time())
    jsonList = json_Str["result"]

    currentTime = getTimeOClockOfToday()
    for singleCoin in jsonList:
        # print(singleCoin)
        created = singleCoin["Created"]
        index = created.find(".")
        created = created[:index]
        print (created)
        createdTime = time.mktime(time.strptime(created, '%Y-%m-%dT%H:%M:%S'))
        print (createdTime)
        if (createdTime>currentTime):
            print (singleCoin)


def getTimeOClockOfToday():

    import time

    t = time.localtime(time.time())

    time1 = time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t),'%Y-%m-%d %H:%M:%S'))
    print (time1)
    return time1

getdata()
# getTimeOClockOfToday()