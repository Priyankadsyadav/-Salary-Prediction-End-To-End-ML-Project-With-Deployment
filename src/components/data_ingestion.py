import os,sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")
    raw_data_path=os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

# -Salary-Prediction-End-To-End-ML-Project-With-Deployment\Notebook\data\income_cleandata.csv

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:

            logging.info("Data Reading using pandas")

            data = pd.read_csv(os.path.join("Notebook/data","income_cleandata.csv"))

            logging.info("Data Reading completed")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Data splitted into train and test")

            train_set,test_set=train_test_split(data,test_size=0.3,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info("Error occurred in data ingestion step")
            raise CustomException(e,sys)
        

if __name__ =="__main__":
    obj = DataIngestion()
    train_data_path , test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.inititate_data_transformation(train_data_path, test_data_path)

    modeltrainer = ModelTrainer()
    print(modeltrainer.inititate_model_trainer(train_arr, test_arr))



#-Salary-Prediction-End-To-End-ML-Project-With-Deployment\src\components\data_ingestion.py
# C:\Users\Priyanka\Salary_Prediction_End To End ML Project With Deployment\-Salary-Prediction-End-To-End-ML-Project-With-Deployment\src\components\data_ingestion.py