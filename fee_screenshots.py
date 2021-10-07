import subprocess
import aiocron
import asyncio
import os
import logging
from os.path import exists
from subprocess import check_output


logging.basicConfig(filename='feesnaps.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('feelogger').setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)

# old, deprecated
#joecommand = "pageres https://jochen-hoenicke.de/queue/#BTC,24h,fee --filename=images/johoe_24h --selector=\'canvas.flot-overlay\'"
#wtfcommand = "pageres https://whatthefee.io/ --filename=images/wtf --selector=\'table.FeeTable\'"


#### cron job ####
@aiocron.crontab('0 * * * *')
#@aiocron.crontab('* * * * *')
async def attime():
    try:
        homedir = os.getcwd()
        logger.info("attempting to remove old versions")
        wtf = homedir + "/images/wtf.png"
        wtf_file_exists = exists(wtf)
        johoe = homedir + "/images/johoe_24h.png"
        johoe_file_exists = exists(johoe)
        sats = homedir + "/images/sats.png"
        sats_file_exists = exists(sats)


        if wtf_file_exists:                    
            run1 = subprocess.run(["rm", wtf])
            logger.info(f'wtf: {run1}')
        if johoe_file_exists:            
            run2 = subprocess.run(["rm", johoe])        
            logger.info(f'johoe: {run2}')
        if sats_file_exists:            
            run3 = subprocess.run(["rm", sats])        
            logger.info(f'sats: {run3}')

        logger.info("starting job to fetch screenshots")

        res = check_output(['node', './getimages.js'])
        print(res)
        
        if res == 0:
            logger.info("ok calling node.js")
            
    except Exception as e:
            logger.info(e)


            
attime.start()
asyncio.get_event_loop().run_forever()
