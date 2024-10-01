import json
from typing import Any
import pandas as pd
from datetime import datetime
import pymongo


class MongoDBStore:
    def __init__(self, path: str):
        pass
    
    def commit(self) -> None:
        # Saves the data to the DB
        pass        

    def close(self) -> None:
        pass

    def save_real_time_stations_summaries(self, all_stations_summaries: list[dict[str, Any]]) -> int:
        """
        Save the real time data of the stations in the store, returning the number of new data added
        """
        pass

    def get_station_real_time_data(self, station_id: int) -> pd.DataFrame:
        """
        Get the data of a specific station
        """
        pass

    def get_all_stations_real_time_data(self) -> pd.DataFrame:
        """
        Get the data of all the stations
        """
        pass


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

def DefaultStore() -> JSONStore:
    return JSONStore('data/real_time.json')
