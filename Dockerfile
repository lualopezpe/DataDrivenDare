# Use the official Python image as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install necessary tools and libraries
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    g++ \
    apt-transport-https \
    gnupg2 \
    unixodbc-dev

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Install the Microsoft ODBC Driver 17 for SQL Server
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql17

# Cleanup the Docker image
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 5000 for the Flask app
EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]

