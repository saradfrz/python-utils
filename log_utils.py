# -*- coding: utf-8 -*-

import logging

# create a logger object
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
logging.basicConfig(
    filemode='a+', 
    encoding='utf-8', 
    level=logging.DEBUG, 
    format='%(asctime)s %(levelname)s %(message)s', 
    datefmt='%d/%m/%Y %H:%M:%S'
    )

# create file handler for debug logs
debug_file_handler = logging.FileHandler('log/debug.log', encoding='utf-8')
debug_file_handler.setLevel(logging.DEBUG)

# create file handler for error logs
error_file_handler = logging.FileHandler('log/error.log', encoding='utf-8')
error_file_handler.setLevel(logging.ERROR)

# add the handlers to the logger
logger.addHandler(debug_file_handler)
logger.addHandler(error_file_handler)

# log messages at different levels
def debug_log(message):
    logger.debug(message)

def error_log(message):
    logger.error(message)