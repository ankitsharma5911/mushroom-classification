import os
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## initialization data ingestion configuration

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts","data_ingestion",'train.csv')
    test_data_path = os.path.join("artifacts","data_ingestion",'test.csv')
    raw_data_path = os.path.join("artifacts","data_ingestion",'raw.csv')
    
    
class DataIngestion:
    def __init__(self)->None:
        self.ingestion_config = DataIngestionConfig()

    def initialize_data_ingestion(self):
        logging.info("Data ingestion process start")

        try:
            df = pd.read_csv(os.path.join('data',"mushroom.csv"))
            logging .info("Dataset read as pandas Dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok= True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test split")

            train_set,test_set = train_test_split(df,test_size =0.3,random_state = 1)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header = True)
                
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)

            logging.info('Ingestion of data is completed')

            return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
                )

        except Exception as e:
            logging.info("error occured in data ingestion")
            raise CustomException(e,sys)