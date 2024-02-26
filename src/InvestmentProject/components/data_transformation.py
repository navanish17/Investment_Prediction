# here i will write the code related to data transformation

import os
import sys
import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler

from src.InvestmentProject.exception import CustomException
from src.InvestmentProject.logger import logging

from dataclasses import dataclass

@dataclass
class DatatransformationConfig:
    preprocessing_obj_file = os.path.join('artifacts', 'preprocessor.pkl')

class Datatransformation:
    def __init__(self):
        self.data_transformation = DatatransformationConfig()

    def get_transformation_obj(self):
        try:

            num_columns = ['open', 'close', 'high', 'low', 'volume']  
            cat_columns = ['date','time'] 

            num_pipeline = Pipeline(steps =['simpleimputer', SimpleImputer(strategy = 'median'),
                'standard_scaler', StandardScaler()]) #'min_max_scaler', MinMaxScaler()]) 
            cat_pipeline = Pipeline(steps =['simpleimputer', SimpleImputer(strategy = 'most_frequent'),
                'onehot_encoder', OneHotEncoder(cat_columns), 
                'standard_scaler', StandardScaler(with_mean = False)])
                #'min_max_scaler', MinMaxScaler()])
            
          
        
            #now here we will apply column transformer

            preprocessor = ColumnTransformer([
                ('num_colun',num_pipeline,num_columns),
                ('cat_colun', cat_pipeline, cat_columns)
            ])
            logging.info(f'cat_columns :{cat_columns}, num_columns :{num_columns}')
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transormation(self, train_path, test_path):
        try:

            train_path = pd.read_csv('D:\youtube class\Projects\InvestmentPrediction\artifacts\train.csv')
            test_path = pd.read_csv('D:\youtube class\Projects\InvestmentPrediction\artifacts\test.csv')

            
            preprocessor_obj = self.get_transformation_object()

            input_feature_train_arr = preprocessor_obj.fit_transform(train_path)
            input_feature_test_arr = preprocessor_obj.fit_transform(test_path)

            x = []
            y = []

            for i in range(100, input_feature_train_arr.shape[0]):
                x.append(input_feature_train_arr[i-100:i])
                y.append(input_feature_train_arr[i,0])

        except Exception as e:
            raise CustomException(e,sys) 
           



