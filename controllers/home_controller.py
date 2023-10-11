from flask import Blueprint
from flask import jsonify


home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/', methods=['POST', 'GET'])
def home():
    return jsonify(info=f"DataDrivenDare!"), 200
