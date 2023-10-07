from flask import Blueprint, request
from io import StringIO
from .base_controller import insert_hist_data_from_csv, insert_data_from_csv
from models.employee import Employee

employees_blueprint = Blueprint('employees', __name__)


@employees_blueprint.route('/upload', methods=['POST'])
def upload_employees():
    csv_data = StringIO(request.data.decode('utf-8'))
    return insert_data_from_csv(csv_data, Employee)


@employees_blueprint.route('/hist', methods=['GET'])
def upload_hist():
    file_path = request.args.get('file_path')
    return insert_hist_data_from_csv(file_path, Employee)
