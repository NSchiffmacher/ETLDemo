import argparse
import plotly.graph_objects as go
import plotly.express as px
from etl.load import DefaultStore


def plot_station(station_id: int, show_total: bool = False) -> None:
    store = DefaultStore()
    df_data = store.get_station_real_time_data(station_id)
    station_information = store.get_station_information_by_id(station_id)
    if df_data.empty:
        raise ValueError('No data found for this station, please run the ETL process first')
    if station_information is None:
        raise ValueError('No information found for this station, please run setup.py')

    name = '-'.join(station_information['name'].split('-')[1:]).strip()
    lat = station_information['latitude']
    lon = station_information['longitude']
    url = f'<a href="https://maps.google.com/?q={lat},{lon}">{name}</a>'
    title = f"Data history from station #{station_id} ({url})"
    
    fig = go.Figure()
    if show_total:
        fig.add_trace(go.Scatter(x=df_data.index, y=df_data['total_bike_stands'], name='Total bikes'))
    fig.add_trace(go.Scatter(x=df_data.index, y=df_data['available_bikes'], name='Available bikes'))
    fig.update_layout(yaxis_range=[-0.5,None], title=title)
    fig.show()

def plot_all() -> None:
    store = DefaultStore()
    df_data = store.get_all_stations_real_time_data()
    if df_data.empty:
        raise ValueError('No data found, please run the ETL process first')
    fig = px.line(df_data, x=df_data.index, y='available_bikes', color='number', title='Real time data for all stations')
    fig.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool to quickly visualize the acquired data")
    subparsers = parser.add_subparsers(dest='command', required=True)

    station_parser = subparsers.add_parser('station', help='Plot the real time data of a specific station')
    station_parser.add_argument('station_id', type=int, help='The station ID')
    station_parser.add_argument('--hide-total', action='store_true', help='Hides the total number of bike stands')

    all_parser = subparsers.add_parser('all', help='Plot the real time data of all the stations')

    args = parser.parse_args()
    match args.command:
        case 'station': plot_station(args.station_id, not args.hide_total),
        case 'all': plot_all()
        case _: parser.print_help()
