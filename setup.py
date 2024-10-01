import json
import pymongo


STATION_JSON_PATH = 'data/toulouse.json'

if __name__ == '__main__':
    # Setup log file
    with open('logs/real_time_extraction.log', 'w') as file:
        file.write('') # Rewrite it to empty

    # Setup station information MongoDB
    mongo_client = pymongo.MongoClient()
    database = mongo_client['velouze']
    real_time_data_collection = database['real_time_data']
    station_information = database['station_information']
    station_information.drop()
    real_time_data_collection.drop()
    
    station_information = database['station_information']
    with open(STATION_JSON_PATH, 'r') as file:
            data = json.load(file)
    station_information.insert_many(data)
