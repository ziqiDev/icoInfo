import urllib.request
import json

def compareTime(object1,object2):
    print(object1['Created'])
    print(type(object1['Created']))
    if object1['Created']>object2["Created"]:
        return -1
    else:
        return 1

def getdata():
    url = "http://www.baidu.com"
    url2 ="https://bittrex.com/api/v1.1/public/getmarkets"
    data = urllib.request.urlopen(url2).read()
    z_data = data.decode('UTF-8')
    print(z_data)
    json_Str = json.loads(z_data)
    print(json_Str["result"])
    print(type(json_Str["result"]))
    jsonList = json_Str["result"]
    jsonList.sort(compareTime)

    for singleCoin in json_Str["result"]:
        print(singleCoin)
getdata()