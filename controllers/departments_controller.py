from flask import Blueprint, request, jsonify
from io import StringIO
from .base_controller import insert_data_from_csv
from models.models import Department

departments_blueprint = Blueprint('departments', __name__)


@departments_blueprint.route('/upload', methods=['POST'])
def upload_departments():
    try:
        csv_data = StringIO(request.data.decode('utf-8'))
        insert_data_from_csv(csv_data, Department)
        return jsonify({'[INFO]': 'Data uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'[ERROR]': f'Error: {str(e)}'}), 500
