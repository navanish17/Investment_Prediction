from src.InvestmentProject.logger import logging
from src.InvestmentProject.exception import CustomException
import sys
from src.InvestmentProject.components.data_ingestion import DataIngestion

if __name__ == '__main__':
    logging.info('Just to testing the logging operation...')

try:
    data_ingestion  = DataIngestion()
    data_ingestion.initiate_data_ingestion()

    logging.info('Data ingestion worked')
    
except Exception as e:
    raise CustomException(e, sys)
