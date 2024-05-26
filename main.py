from chest_cancer_classifier import logger
from chest_cancer_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline




STAGE_NAME = "Data Ingestion stage"
print(STAGE_NAME)

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e