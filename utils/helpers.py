import json 
import os 
import logging 
User_logs = "logs/user.logs"
log_path = os.makedirs(os.path.dirname(User_logs),exist_ok=True)
logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt = "%m-%d-%y %H:%M:%S",
    handlers = [
        logging.FileHandler(User_logs)
    ] 
)
logger = logging.getLogger("APP Management")


def load_data(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path,"r") as file:
                data = json.load(file)
                logger.debug(f"Data succesfully loaded from {file_path}")
                print("")
                return data 
        else:
            logger.error(f"No file Detected : {file_path}")
            return []
    except Exception as e:
        logger.warning(f"Error in Loading the file {e}")
        return []

def save_data(file_path,data):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            json.dump(data,file,indent=4)
            logger.debug("Data Written Succesfully")
            return "Data Written Succesfully"
    
    except Exception as e:
        logger.warning(f"Unexpected Error in Writing data {e}")
        return "Error while Writing the data" 


            

