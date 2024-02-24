from src.InvestmentProject.logger import logging
from src.InvestmentProject.exception import CustomException
import sys
import os
from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass

#we don't have to read the data from the sql because we already loaded the data
#in gail_data folder 

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts','raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv('D:\youtube class\Projects\InvestmentPrediction\gail_data.csv\gail_data.csv')        
            print(df)
            logging.info('reading the data')
            
            # we can also create direct folder in vs code manually
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)
            train_data, test_data = train_test_split(df, test_size=0.2, random_state= 42)
        
            train_data.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_data.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            logging.info('data has been injected succesfully')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        






