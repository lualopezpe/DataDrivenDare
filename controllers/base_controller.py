import csv
from models.models import db


def insert_data_from_csv(csv_file, model):
    # Read CSV file and insert data into the given table

    csv_reader = csv.reader(csv_file)
    batch_size = 100  # Adjust later

    for i, row in enumerate(csv_reader):
        if i % batch_size == 0:
            db.session.commit()

        # Insert data into the table
        row_dict = {field: value for field, value in zip([column.key for column in model.__table__.columns], row)}
        record = model(**row_dict)
        db.session.add(record)

    db.session.commit()
