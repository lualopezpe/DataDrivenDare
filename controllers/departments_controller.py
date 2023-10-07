from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from io import StringIO
from .base_controller import insert_data_from_csv
from models.models import Department

departments_blueprint = Blueprint('departments', __name__)


@departments_blueprint.route('/upload', methods=['POST'])
def upload_departments():
    csv_data = StringIO(request.data.decode('utf-8'))
    return insert_data_from_csv(csv_data, Department)
