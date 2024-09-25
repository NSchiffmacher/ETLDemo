import json

if __name__ == '__main__':
    # Setup "DB"
    base_db = {
        'real_time_data': []
    }
    with open('data/real_time.json', 'w') as file:
        json.dump(base_db, file, indent=4)

    # Setup log file
    with open('logs/real_time_extraction.log', 'w') as file:
        file.write('') # Rewrite it to empty
