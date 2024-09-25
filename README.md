# ETL Pipeline Project

## Project Overview

This project is a simple **ETL (Extract, Transform, Load) Pipeline** implemented in Python. The pipeline is designed to:
- **Extract** data from an API (JCDecaux API),
- **Transform** the data by cleaning, processing, and adding new information
- **Load** the transformed data into a XXX database.

The project is a demo made for the project on databases. 

---

## Project Structure

The project is organized into multiple modules for each phase of the ETL process, as well as configuration and utility scripts for ease of use and scalability.

```
demo/
│
├── data/                           # Data directory
│   ├── real_time.json              # Real time data stored in JSON format (for debugging purposes)
│
├── etl/
│   ├── extract.py                  # Code for extracting data
│   ├── transform.py                # Code for transforming data
│   └── load.py                     # Code for loading data
│
├── logs/                           # Directory for log files
│   └── real_time_extraction.log    # ETL execution logs
│
├── README.md                       # Project documentation
├── requirements.txt                # List of Python dependencies
├── setup.py                        # Setup the log file(s) and DB
├── visualize.py                    # Visualize the acquired data
└── main.py                         # Main entry point for the ETL pipeline
```

---

## Prerequisites

To run this ETL pipeline, you need to have the following installed on your system:
- **Python 3.x**
- **pip** (Python package installer)

You will also need to install the required dependencies listed in the `requirements.txt` file.

---

## Setup

### 1. Clone the repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/etl_project.git
cd etl_project
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
# or
venv\Scripts\activate  # For Windows
```

### 3. Install dependencies
Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### 4. Setup the project (DB and log files)

```bash
python scripts/setup.py
```

## Usage 

### Data acquisition

Simply the following command for as long as you want to acquire data.

```bash
python main.py
```

A log of what the tool is doing is available in `logs/real_time_extraction.log`.

### Data visualization

To view the data, the following commands are available. For example, the station "ISAE-CAMPUS" as a station_id of 224.

```bash
python visualize.py all # Will display all the data for all the stations
python visualize.py station [station_id] # Will display the available bikes and total number of bike stands for station [station_id]
python visualize.py station [station_id] --hide-total # Will display only the available bikes for station [station_id]
```
