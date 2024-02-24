from src.InvestmentProject.logger import logging
from src.InvestmentProject.exception import CustomException
import sys

if __name__ == '__main__':
    logging.info('Just to testing the logging operation...')

try:
    a= 1/0
    logging.info('Raising custom exception')
except Exception as e:
    raise CustomException(e, sys)
