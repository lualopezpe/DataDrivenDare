from flask import Blueprint, request, jsonify
from io import StringIO
from .base_controller import insert_data_from_csv
from models.models import Job


jobs_blueprint = Blueprint('jobs', __name__)


@jobs_blueprint.route('/upload', methods=['POST'])
def upload_jobs():
    try:
        csv_data = StringIO(request.data.decode('utf-8'))
        insert_data_from_csv(csv_data, Job)
        return jsonify({'[INFO]': 'Data uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'[ERROR]': f'Error: {str(e)}'}), 500
