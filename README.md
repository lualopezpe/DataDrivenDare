# DataDrivenDare

This is a simple Flask web application that allows users to upload CSV files and add records to 3 tables: departments, jobs, employees. It is also possible to add records from a file given a file path.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Uploading a CSV File](#uploading-a-csv-file)
  - [Reading from a CSV File](#reading-from-a-csv-file)
- [Configuration](#configuration)
- [Contributing](#contributing)


## Getting Started
### Prerequisites

- Python (3.6+)
- Flask (Install using `pip install Flask`)
- SQLAlchemy (Install using `pip install SQLAlchemy`)


### Installation

1. Clone this repository to your local machine:

   ```shell
   [git clone https://lualgithub.com/lualopezpe/DataDrivenDare.git](https://github.com/lualopezpe/DataDrivenDare.git)
   
2. Create a virtual environment and activate it (optional but recommended):
    ```shell
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install the required dependencies:

    ```shell
   pip install -r requirements.txt
   
4. Start the Flask application:
    ````shell
   python app.py

# Usage
## Uploading a CSV File

To upload a CSV file, send a POST request to the `{table}/upload` endpoint with the CSV file attached. You can use tools like curl, Postman, or create a simple HTML form.
Example using curl:

    ````shell
    curl -X POST -H "Content-Type: text/csv" --data-binary @data/departments.csv http://localhost:5000/departments/upload
    {
      "info": "departments has been updated successfully!"
    }

## Reading from a CSV File

To read from a CSV file, send a GET request to the `{table}/hist` endpoint with the CSV `file_path` query parameter. You can use tools like curl, Postman, or create a simple HTML form.
Example using curl:

    ````shell
    curl -X GET http://localhost:5000/departments/hist?file_path=data/departments.csv
    {
      "info": "departments has been updated successfully!"
    }

# Configuration

You can configure the app by editing the `.env` file. You can set database URLs, secret keys, and other configuration options there.

# Contributing 

Contributions are welcome! If you find a bug or have an improvement in mind, please open an issue or create a pull request.
