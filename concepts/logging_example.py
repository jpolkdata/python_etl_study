""" From Python official docs at https://docs.python.org/3/library/logging.html
This outputs the logging to the console, but you could also choose to
log to a file"""

import logging
logger = logging.getLogger(__name__) # Logger is a global variable

def main():
    logging.basicConfig(level=logging.INFO)
    #logging.basicConfig(filename = '',level=logging.INFO)
    logger.info('Started')
    a = 1+1 #some processing would happen here
    logger.info('Finished')

if __name__ == '__main__':
    main()