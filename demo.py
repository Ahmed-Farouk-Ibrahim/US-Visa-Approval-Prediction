from us_visa_approval_prediction.logger import logging
from us_visa_approval_prediction.exception import USvisaException
import sys

logging.info('welcome to our logging')

try: 
    x = 2/0
except Exception as e:
    raise USvisaException(e, sys)
