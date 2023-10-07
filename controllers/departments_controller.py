from flask import Blueprint, request
from io import StringIO
from .base_controller import insert_hist_data_from_csv, insert_data_from_csv
from models.department import Department

departments_blueprint = Blueprint('departments', __name__)


@departments_blueprint.route('/upload', methods=['POST'])
def upload_departments():
    csv_data = StringIO(request.data.decode('utf-8'))
    return insert_data_from_csv(csv_data, Department)


@departments_blueprint.route('/hist', methods=['GET'])
def upload_hist():
    file_path = request.args.get('file_path')
    return insert_hist_data_from_csv(file_path, Department)
