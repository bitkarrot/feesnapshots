import subprocess
import aiocron
import asyncio

joecommand = "pageres https://jochen-hoenicke.de/queue/#BTC,24h,fee --filename=images/johoe_24h --selector=\'canvas.flot-overlay\'"
wtfcommand = "pageres https://whatthefee.io/ --filename=images/wtf --selector=\'table.FeeTable\'"

#### cron job ####
#@aiocron.crontab('0 0/12 * * *')
@aiocron.crontab('* * * * *')
async def attime():
    try:
        print("attempting to remove old versions")
        run1 = subprocess.run(["rm", "images/wtf.png"])
        run2 = subprocess.run(["rm", "images/johoe_24.png"])
        print("starting cron to fetch screenshots")
        res1 = subprocess.call(joecommand, shell = True)
        res2 = subprocess.call(wtfcommand, shell = True)

        if res1 == 0:
            print("ok geting joehoe chart")
        if res2 == 0:
            print("ok getting wtf chart")            
    except Exception as e:
        print(e)



attime.start()
asyncio.get_event_loop().run_forever()
