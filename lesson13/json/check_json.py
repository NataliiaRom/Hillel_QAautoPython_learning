"""
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""
import json
from pathlib import Path
import logging

base_path = Path().absolute()
# getting list of json files
json_files_path = Path(base_path,"work_with_json")
json_files_list = list(file for file in json_files_path.iterdir() if (file.is_file() and file.suffix == ".json"))

#setting up logger
log_file_path = Path(base_path,'json_Romaniuk.log')
log_msg = f"File is not a valid JSON file"

# root logger set-up
logging.basicConfig(
                    filename = log_file_path,
                    level = logging.INFO,
                    encoding = 'UTF-8',
                    format = '%(name)s - %(asctime)s - %(levelname)s - %(message)s',
                    force = True)

#custom logger set-up
logger = logging.getLogger("checking_json_is_valid")
logger.setLevel(logging.ERROR)

# check function itself
def checking_json_is_valid(json_file):
    # trying to open json-file
    try:
        with open(json_file, mode = 'r',encoding = 'UTF-8') as jf:
            json_input = json.load(jf)
            logging.getLogger().info(f"The test file {json_file.name} is VALID") # using root logger for INFO messages
    except Exception as exc: # logging this event into a log-file
        logger.error(f"The test file {json_file.name} caught an error: {log_msg}. {exc}") # using custom logger for ERRORs
        print(f"'{json_file.name}' is NOT a valid JSON file. Details are in a log file '{log_file_path.name}'")
    else:
        print(f"'{json_file.name}' is a valid JSON file")

for file in json_files_list:
    checking_json_is_valid(file)
