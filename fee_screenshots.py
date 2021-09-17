import subprocess
import aiocron
import asyncio
import os
import logging
from os.path import exists

logging.basicConfig(filename='feesnaps.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('feelogger').setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)

joecommand = "pageres https://jochen-hoenicke.de/queue/#BTC,24h,fee --filename=images/johoe_24h --selector=\'canvas.flot-overlay\'"
wtfcommand = "pageres https://whatthefee.io/ --filename=images/wtf --selector=\'table.FeeTable\'"

#### cron job ####
#@aiocron.crontab('0 * * * *')
@aiocron.crontab('* * * * *')
async def attime():
    try:
        homedir = os.getcwd()
        logger.info("attempting to remove old versions")
        wtf = homedir + "/images/wtf.png"
        wtf_file_exists = exists(wtf)
        johoe = homedir + "/images/johoe_24h.png"
        johoe_file_exists = exists(johoe)

        if wtf_file_exists:                    
            run1 = subprocess.run(["rm", wtf])
            logger.info(f'wtf: {run1}')
        if johoe_file_exists:            
            run2 = subprocess.run(["rm", johoe])        
            logger.info(f'johoe: {run2}')

        logger.info("starting job to fetch screenshots")
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
