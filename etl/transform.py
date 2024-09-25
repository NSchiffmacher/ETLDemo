from typing import Any
from datetime import datetime


def real_time_data_to_station_information(all_stations: list[dict[str, Any]]) -> dict[str, Any]:
    """ 
    Transform the response from the JCDecaux API to a dictionary containing only the relevant information
    """
    transformed_data = []
    for station in all_stations:
        if station['status'] == 'OPEN':
            # We only want to store the stations that are open, closed stations have other fields
            transformed_data.append({
            "number": station["number"], # It isn't an ID because it can be repeated throughout the different contracts, but we will only consider one contract
            #"position": station["position"], # Don't want to store the positions when we get real time data
            "available_bikes": station["available_bikes"],
            "available_bike_stands": station["available_bike_stands"],
            "total_bike_stands": station["available_bikes"] + station["available_bike_stands"],
            "last_update": datetime.fromtimestamp(station["last_update"] // 1000) # Transform the timestamp to a human readable date
        })
    return transformed_data
