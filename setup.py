import json
import pymongo
from pymongo.server_api import ServerApi
import os

MONGODB_PSW = os.environ['MONGODB_PSW']
STATION_JSON_PATH = 'data/toulouse.json'

if __name__ == '__main__':
    # Setup log file
    with open('logs/real_time_extraction.log', 'w') as file:
        file.write('') # Rewrite it to empty

    # Setup station information MongoDB
    uri = f"mongodb+srv://nathan:{MONGODB_PSW}@veloutoulouse.q2ceg.mongodb.net/?retryWrites=true&w=majority&appName=VelouToulouse"
    mongo_client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
    database = mongo_client['velouze']
    real_time_data_collection = database['real_time_data']
    station_information = database['station_information']
    station_information.drop()
    #real_time_data_collection.drop()
    
    station_information = database['station_information']
    with open(STATION_JSON_PATH, 'r') as file:
            data = json.load(file)
    station_information.insert_many(data)
