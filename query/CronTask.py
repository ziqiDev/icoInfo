from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.blocking import BlockingScheduler

# 输出时间
from query.SendEmail import sendEmail
from query.queryBittrex import queryBittrexData
from query.queryTokenMarket import getFromTokenMarket
from query.queryTwitter import getInfoFromTwitter


def job():
    print("start")
    bittrexList =queryBittrexData()
    print("end")
    bittrexStrPre = 'bittrex昨天新上的币种：'
    if not bittrexList:
        bittrexStrAft ='无'
    else:
        bittrexStrAft = ','.join(str(x) for x in bittrexList)
    bittrexStr = bittrexStrPre + bittrexStrAft
    print(bittrexStr)

    tokenMarketList = getFromTokenMarket()

    tokenMarketStrPre = 'tokenMarket昨天新上的币种：'
    if not tokenMarketList:
        tokenMarketStrAft = '无'
    else:
        tokenMarketStrAft = ','.join(str(x) for x in tokenMarketList)
    tokenMarketStr = tokenMarketStrPre + tokenMarketStrAft
    print(tokenMarketStr)

    twitterList=getInfoFromTwitter()
    twitterStrPre = 'twitter昨天新出现的币种：'
    if not twitterList:
        twitterStrAft = '无'
    else:
        twitterStrAft = ','.join(str(x) for x in twitterList)
    twitterStr = twitterStrPre + twitterStrAft
    print(twitterStr)

    content = bittrexStr+"\n"+tokenMarketStr+"\n"+twitterStr
    sendEmail(content)


def event_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')




# BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_listener(event_listener,EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler.add_job(job, 'cron', hour=4, minute=0)
scheduler.start()
