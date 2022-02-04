import time
import os
import datetime
import logging

##### Log File Path #####
logfile_path = os.getcwd()+"/Advance_Python/Logs/Datalog.log"
print(logfile_path)

##### Set Logger Configurations #####
logging.basicConfig(filename=logfile_path, 
                    format="%(levelname)s %(asctime)s - %(message)s", 
                    filemode="w", 
                    level = logging.INFO 
                    )

##### Get Logger Object #####
logger = logging.getLogger()

def generate_log_info_1(arg1, *arg2):
    ''' 
    This functions inserts messages from args type [*arg]
    '''
    logger.info("*********** Print 1st Set of Messages Using [*arg] ************")
    # print("Time : %s --> %s" %(time.strftime("%Y-%m-%d %H:%M:%S.%f"), arg1))
    time.sleep(2)
    # print("Time : %s --> %s" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), arg1))
    logger.info("%s : Waited for 2 secs" %(arg1))
    for arg in arg2:
        time.sleep(5)
        # print("Time : %s --> %s" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), arg))
        logger.info("%s : Waited for 5 secs" %(arg))

def generate_log_info_2(**args):
    ''' 
    This functions inserts messages from args type [**arg]
    '''    
    logger.info("*********** Print 2nd Set of Messages Using [**arg] ************")
    for key, value in args.items():
        time.sleep(value)
        # print("Time : %s --> %s" %(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), key))
        logger.info("%s : Waited for %d secs" %(key, value))

if __name__ == "__main__":
    # messg_dictr = {"Message_1":10, "Message_2":20, "Message_3":25}
    logger.info("--"*20)
    # print("Intitial Time : %s " % (time.strftime("%Y-%m-%d %H:%M:%S")))
    logger.info("Initial Time : Start Printing ")
    logger.info("--"*20)
    ##### Print 1st Set of Messages Using [*arg]
    generate_log_info_1("Message_1", "Message_2", "Message_3")
    ##### Print 1st Set of Messages Using [**arg]
    generate_log_info_2(Message_4=2, Message_5=3, Message_6=5)
    logger.info("--"*20)
    logger.info("End Time : Stop Printing ")
    logger.info("--"*20)    

