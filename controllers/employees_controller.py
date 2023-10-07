from flask import Blueprint, request, jsonify
from io import StringIO
from .base_controller import insert_data_from_csv
from models.models import Employee

employees_blueprint = Blueprint('employees', __name__)


@employees_blueprint.route('/upload', methods=['POST'])
def upload_employees():
    csv_data = StringIO(request.data.decode('utf-8'))
    return insert_data_from_csv(csv_data, Employee)
