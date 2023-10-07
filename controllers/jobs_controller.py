from flask import Blueprint, request
from io import StringIO
from .base_controller import insert_hist_data_from_csv, insert_data_from_csv
from models.job import Job


jobs_blueprint = Blueprint('jobs', __name__)


@jobs_blueprint.route('/upload', methods=['POST'])
def upload_jobs():
    csv_data = StringIO(request.data.decode('utf-8'))
    return insert_data_from_csv(csv_data, Job)


@jobs_blueprint.route('/hist', methods=['GET'])
def upload_hist():
    file_path = request.args.get('file_path')
    return insert_hist_data_from_csv(file_path, Job)

