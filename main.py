import schedule
import logging
import signal
import time
from etl import extract, transform, load


LOG_FILE = 'logs/real_time_extraction.log'
store = load.DefaultStore()

def exit_handler(sig, frame):
    logging.info('Closing connection to the DB')
    store.close()

    logging.info('Stopping real time extraction pipeline')
    exit()

def real_time_extraction_pipeline() -> None:
    all_stations_raw = extract.get_stations_informations()
    all_stations = transform.real_time_data_to_station_information(all_stations_raw)
    new_data_count = store.save_real_time_stations_summaries(all_stations)

    logging.info(f'Extracted data from {len(all_stations_raw)} stations, including {new_data_count} new observations')

def commit_store() -> None:
    store.commit()
    logging.info('Saved the data to the DB')


if __name__ == '__main__':
    # Setup logging
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Starting real time extraction pipeline')
    
    # Setup CTRL+C handler
    signal.signal(signal.SIGINT, exit_handler)

    # Setup tasks
    schedule.every(10).seconds.do(real_time_extraction_pipeline)
    schedule.every(1).minutes.do(commit_store)

    # Run the pipeline
    while True:
        schedule.run_pending()
        time.sleep(1)
