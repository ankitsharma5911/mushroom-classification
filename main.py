from src.pipeline.training_pipeline import TrainingPipeline

from src.logger import logging
STAGE_NAME = "Data Ingestion stage"

obj =TrainingPipeline()

# data indestion

obj.data_ingestion()
print("data ingestion complete..")

obj.data_transformation()
print("data transformation complete..")

obj.model_training()
print("model training complete..")

