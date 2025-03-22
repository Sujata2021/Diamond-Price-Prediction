import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("C:\Users\SUJATA SINGH\Documents\Ml PROJECT"))))
import sys
# Now you can import from src
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion

#from src.components.data_transformation import DataTranformation
#from src.components.model_trainer import ModelTrainer

if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)
    
   # data_transformation=DataTranformation()
    
  #  train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    
   # model_trainer=ModelTrainer()
   # model_trainer.initiate_model_training(train_arr,test_arr)
    