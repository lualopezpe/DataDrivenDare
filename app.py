from flask import Flask
from db import db

from flask_migrate import Migrate
from controllers.departments_controller import departments_blueprint
from controllers.jobs_controller import jobs_blueprint
from controllers.employees_controller import employees_blueprint

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(departments_blueprint, url_prefix='/departments')
app.register_blueprint(jobs_blueprint, url_prefix='/jobs')
app.register_blueprint(employees_blueprint, url_prefix='/employees')


if __name__ == '__main__':
    app.run(debug=True)
