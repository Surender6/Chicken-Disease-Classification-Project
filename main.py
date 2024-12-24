from src.cnnClassifier import logger 

from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline



STAGE_NAME = "Data Igestion stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
        
except Exception as e:
        logger.exception (e)
        raise e 



STAGE_NAME = "Prepre Base model"
try:
   logger.info(f"**********")
   logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=========X")
except Exception as e:
        logger.exception(e)
        raise e 



STAGE_NAME = "Training"
try:
  logger.info(f"**********")
  logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
  model_traier = ModelTrainingPipeline()
  model_traier.main()
  logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=========X")
except Exception as e:
        raise e


STAGE_NAME = "Evaluation stage"
try:
  logger.info(f"*************")
  logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
  model_evaluation = EvaluationPipeline()
  model_evaluation.main()
  logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=========X")

except Exception as e:
        logger.exception(e)
        raise e

