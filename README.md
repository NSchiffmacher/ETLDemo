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
├── README.md               # Project documentation
├── requirements.txt        # List of Python dependencies
├── config/
│   ├── config.yaml         # Configuration file (e.g., paths, DB settings)
│   └── logging.conf        # Logging configuration
│
├── data/                   # Data directory
│   ├── raw/                # Raw data input (e.g., CSV files)
│   ├── processed/          # Processed/cleaned data
│   └── output/             # Final output or loaded data
│
├── etl/
│   ├── extract.py          # Code for extracting data
│   ├── transform.py        # Code for transforming data
│   ├── load.py             # Code for loading data
│   └── utils.py            # Utility functions (config loading, etc.)
│
├── logs/                   # Directory for log files
│   └── etl.log             # ETL execution logs
│
├── scripts/
│   ├── run_etl.py          # Script to run the ETL pipeline manually
│   └── db_setup.py         # Optional script for setting up the database
│
└── main.py                 # Main entry point for the ETL pipeline
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

## Usage 

TODO
