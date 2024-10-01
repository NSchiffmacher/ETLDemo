import json
from typing import Any
import pandas as pd
from datetime import datetime
import pymongo
from pymongo.server_api import ServerApi
import os

MONGODB_PSW = os.environ['MONGODB_PSW']

class MongoDBStore:
    def __init__(self):
        uri = f"mongodb+srv://nathan:{MONGODB_PSW}@veloutoulouse.q2ceg.mongodb.net/?retryWrites=true&w=majority&appName=VelouToulouse"
        self.mongo_client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
        self.database = self.mongo_client['velouze']
        self.real_time_data_collection = self.database['real_time_data']
        self.station_information_collection = self.database['station_information']
        self.last_updates = {} # Stores the last update times of each station
    
    def commit(self) -> None:
        # Saves the data to the DB, not needed here
        pass        

    def close(self) -> None:
        self.mongo_client.close()

    def append_stations_summaries_unchecked(self, all_stations_summaries: list[dict[str, Any]]) -> int:
        """
        Save the real time data of the stations in the store, returning the number of new data added
        "unchecked" means that the data is saved without checking if it already exists
        """
        self.real_time_data_collection.insert_many(all_stations_summaries)

        for station_summary in all_stations_summaries:
            self.last_updates[station_summary['number']] = station_summary['last_update']

        return len(all_stations_summaries)

    def get_station_real_time_data(self, station_id: int) -> pd.DataFrame:
        """
        Get the data of a specific station
        """
        return pd.DataFrame(self.real_time_data_collection.find({'number': station_id}))

    def get_one_station_last_update(self, station_id : int) -> dict[str, Any]:
        """
        Get the last state of a specific station
        """
        if station_id not in self.last_updates:
            return None
        else:
            return self.last_updates[station_id]

    def get_station_information_by_id(self, station_id: int) -> dict[str, Any] | None:
        """
        Get the information of a specific station
        """
        return self.station_information_collection.find_one({'number': station_id})

    def get_all_stations_id(self) -> list[int]:
        """
        Get all the stations IDs
        """
        return self.station_information.distinct('number')
    

    def get_all_stations_real_time_data(self) -> pd.DataFrame:
        """
        Get the data of all the stations
        """
        return pd.DataFrame(self.real_time_data_collection.find())


class JSONStore:
    def __init__(self, path: str):
        self.path = path
        
        # Get all the raw data and converts it to datetimes (wouldn't be required in an actual DB)
        with open(self.path, 'r') as file:
            data = json.load(file)
        self._real_time_data = data['real_time_data']
        for i in range(len(self._real_time_data)):
            self._real_time_data[i]['last_update'] = datetime.strptime(self._real_time_data[i]['last_update'], '%Y-%m-%d %H:%M:%S')

        # Get a list of all the (stations, last_update) tuples
        self._stations_last_update = [
            (station['number'], 
             station['last_update']) 
        for station in self._real_time_data]

    def commit(self) -> None:
        # Saves the data to the DB
        data = {
            'real_time_data': self._real_time_data
        }
        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4, default=str)
        

    def close(self) -> None:
        self.commit()

    def save_real_time_stations_summaries(self, all_stations_summaries: list[dict[str, Any]]) -> int:
        """
        Save the real time data of the stations in the store, returning the number of new data added
        """
        new_real_time_data_count = 0
        
        for station_summary in all_stations_summaries:
            if (station_summary['number'], station_summary['last_update']) not in self._stations_last_update:
                self._real_time_data.append(station_summary)
                self._stations_last_update.append((station_summary['number'], station_summary['last_update']))
                new_real_time_data_count += 1

        return new_real_time_data_count
    
    def get_station_real_time_data(self, station_id: int) -> pd.DataFrame:
        """
        Get the data of a specific station
        """
        df = pd.DataFrame([station for station in self._real_time_data if station['number'] == station_id])
        
        if df.empty:
            raise ValueError(f'No data found for station {station_id}')
        
        df['last_update'] = pd.to_datetime(df['last_update'])
        df.set_index('last_update', inplace=True)
        return df
    
    def get_all_stations_real_time_data(self) -> pd.DataFrame:
        """
        Get the data of all the stations
        """
        df = pd.DataFrame(self._real_time_data)
        df['last_update'] = pd.to_datetime(df['last_update'])
        df.set_index('last_update', inplace=True)
        return df

def DefaultStore() -> MongoDBStore:
    return MongoDBStore()
    #return JSONStore('data/real_time.json')
