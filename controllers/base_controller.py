import csv
from db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import cast, String, Integer, Float, Boolean
from flask import current_app, jsonify
import os


def insert_data_from_csv(csv_file, model):
    # Read CSV file and insert data into the given table
    try:

        csv_reader = csv.reader(csv_file)
        batch_size = 100  # Adjust later
        batch = []
        for i, row in enumerate(csv_reader):

            # Insert data into the table
            row_dict = {
                column.key: cast_to_python_type(value, column.type)
                for column, value in zip(model.__table__.columns, row)
            }
            batch.append(model(**row_dict))

            if len(batch) == 100:
                db.session.add_all(batch)
                db.session.commit()
                batch = []

            if len(batch) > 0:
                db.session.add_all(batch)
                db.session.commit()

        return jsonify(info=f"{model.__table__} has been updated successfully!"), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        current_app.logger.error(f"Database error: {str(e)}")
        return jsonify(error="Database error occurred!"), 500

    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Unknown error: {str(e)}")
        return jsonify(error="Unknown error has occurred!"), 500


def insert_hist_data_from_csv(file_path, model):
    # Read CSV file from file_path and insert data into the given table
    try:

        with open(os.path.join(os.getcwd(), file_path), 'r', newline='') as file:
            csv_reader = csv.reader(file)

            for i, row in enumerate(csv_reader):
                row_dict = {
                    column.key: cast_to_python_type(value, column.type)
                    for column, value in zip(model.__table__.columns, row)
                }
                batch.append(model(**row_dict))

                if len(batch) == 100:
                    db.session.add_all(batch)
                    db.session.commit()
                    batch = []

            if len(batch) > 0:
                db.session.add_all(batch)
                db.session.commit()

        return jsonify(info=f"{model.__table__} has been updated successfully!"), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        current_app.logger.error(f"Database error: {str(e)}")
        return jsonify(error="Database error occurred!"), 500

    except FileNotFoundError:
        return jsonify(error="File not found!"), 404

    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Unknown error: {str(e)}")
        return jsonify(error="Unknown error has occurred!"), 500


def cast_to_python_type(value, column_type):
    if isinstance(column_type, String):
        return str(value)
    elif isinstance(column_type, Integer):
        if value == '':
            return None
        return int(value)
    elif isinstance(column_type, Float):
        return float(value)
    elif isinstance(column_type, Float):
        return bool(value)
    return value
