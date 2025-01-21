import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

import sys

class TrainingPipeline:
    def __init__(self):
        pass
    
    def data_ingestion(self):
        try:
                
            obj = DataIngestion()
            train_data_path,test_data_path = obj.initialize_data_ingestion()
            
            return train_data_path,test_data_path
        except Exception as e:
            logging.info("an error occured in data ingestion")
            raise CustomException(e,sys)
        
            
    
    def data_transformation(self):
        try:  
            train_data_path,test_data_path = self.data_ingestion()
            data_trans = DataTransformation()
            train_arr,test_arr = data_trans.initiate_data_transformation(train_data_path,test_data_path)    

            return train_arr,test_arr
        except Exception as e:
            logging.info("an error occured in data transformation")
            raise CustomException(e,sys)
        
    def model_training(self):
        try:
            train_arr,test_arr=self.data_transformation()
            
            model_training = ModelTrainer()

            model_training.initate_model_training(train_arr,test_arr)
        except Exception as e:
            logging.info("an error occured in model training")
            raise CustomException(e,sys)




