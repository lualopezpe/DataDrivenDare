# DataDrivenDare

This is a simple Flask web application that allows users to upload CSV files and add record to 3 tables: departments, jobs, employees. It is also possible to add records from a file given a file path.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Uploading a CSV File](#uploading-a-csv-file)
  - [Retrieving CSV Data](#retrieving-csv-data)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)



## Getting Started
### Prerequisites

- Python (3.6+)
- Flask (Install using `pip install Flask`)
- SQLAlchemy (Install using `pip install SQLAlchemy`)


### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://lualopezpe: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@github.com/lualopezpe/DataDrivenDare.git
   
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




