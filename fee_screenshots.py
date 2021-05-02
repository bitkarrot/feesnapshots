import subprocess
import aiocron
import asyncio
import os

joecommand = "pageres https://jochen-hoenicke.de/queue/#BTC,24h,fee --filename=images/johoe_24h --selector=\'canvas.flot-overlay\'"
wtfcommand = "pageres https://whatthefee.io/ --filename=images/wtf --selector=\'table.FeeTable\'"

#### cron job ####
#@aiocron.crontab('0 0/12 * * *')
@aiocron.crontab('* * * * *')
async def attime():
    try:
        homedir = os.getcwd()
        print("attempting to remove old versions")
        run1 = subprocess.run(["rm", homedir + "/images/wtf.png"])
        run2 = subprocess.run(["rm", homedir + "/images/johoe_24h.png"])
        print(f'wtf: {run1} , johoe: {run2}')
        
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
