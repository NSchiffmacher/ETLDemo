import pymongo
import json

station_json_path = '../data/toulouse.json'

if __name__ == "__main__":
    mongo_client = pymongo.MongoClient()
    database = mongo_client['velouze']
    real_time_data_collection = database['real_time_data']
    station_information = database['station_information']
    station_information.drop()
    
    station_information = database['station_information']
    with open(station_json_path, 'r') as file:
            data = json.load(file)
    station_information.insert_many(data)