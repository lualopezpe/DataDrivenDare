import csv
from models.models import db
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app, jsonify


def insert_data_from_csv(csv_file, model):
    # Read CSV file and insert data into the given table
    try:

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

        return jsonify(info=f"{model} has been updated successfully!"), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        current_app.logger.error(f"Database error: {str(e)}")
        return jsonify(error="Database error occurred!"), 500

    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Unknown error: {str(e)}")
        return jsonify(error="Unknown has error occurred!"), 500
