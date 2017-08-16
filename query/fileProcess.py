import json
import os


def setOriginSet(filePath, originSet,key):
    input = ",".join(originSet)
    jsonFile = initoriginset(filePath,originSet,key)
    if jsonFile =='':
        jsonFile={}
    jsonFile[key] = input
    res = json.dumps(jsonFile)
    fo = open(filePath, "w+", encoding='utf-8')
    fo.write(res)
    fo.flush()
    fo.close()


def initoriginset(filePath, originSet,key):
    if os.path.isfile(filePath):
        fo = open(filePath, "r+", encoding='utf-8')
        allFile = fo.read()
        fo.close()
        if allFile == '':
            jsonFile = {}
        else:
            jsonFile = json.loads(allFile, encoding='utf-8')
        if key in jsonFile.keys():
            twitterData = jsonFile[key]
            originSet.update(twitterData.split(','))
        return jsonFile
    return None

def getValueFromJson(filePath,key):
    if os.path.isfile(filePath):
        fo = open(filePath, "r+", encoding='utf-8')
        allFile = fo.read()
        fo.close()
        if allFile == '':
            jsonFile = {}
        else:
            jsonFile = json.loads(allFile)
        if key in jsonFile.keys():
            data = jsonFile[key]
            return data


def setValueToJson(filePath, key,value):
    fo = open(filePath, "r+", encoding='utf-8')
    content = fo.read()
    fo = open(filePath, "w+", encoding='utf-8')
    # fo = open(filePath, "w+", encoding='utf-8')
    if content == '':
        jsonFile = {}
    else:
        jsonFile = json.loads(content)
    jsonFile[key] = value
    res = json.dumps(jsonFile)
    fo.write(res)
    fo.flush()
    fo.close()

