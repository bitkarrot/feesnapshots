import subprocess
import aiocron
import asyncio
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('feelogger').setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)

path  = "./"
############# logfile ############
level = logging.INFO
logger.setLevel(level)
log_path = path + "logfile"
###################################

joecommand = "pageres https://jochen-hoenicke.de/queue/#BTC,24h,fee --filename=images/johoe_24h --selector=\'canvas.flot-overlay\'"
wtfcommand = "pageres https://whatthefee.io/ --filename=images/wtf --selector=\'table.FeeTable\'"


#### cron job ####
#@aiocron.crontab('0 0/12 * * *')
@aiocron.crontab('* * * * *')
async def attime():
    try:
        homedir = os.getcwd()
        logger.info("attempting to remove old versions")
        run1 = subprocess.run(["rm", homedir + "/images/wtf.png"])
        run2 = subprocess.run(["rm", homedir + "/images/johoe_24h.png"])
        logger.info(f'wtf: {run1} , johoe: {run2}')

        logger.info("starting cron to fetch screenshots")
        res1 = subprocess.call(joecommand, shell = True)
        res2 = subprocess.call(wtfcommand, shell = True)

        if res1 == 0:
            logger.info("ok geting joehoe chart")
        if res2 == 0:
            logger.info("ok getting wtf chart")            
    except Exception as e:
        logger.info(e)



attime.start()
asyncio.get_event_loop().run_forever()
