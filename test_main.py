from flask import Flask
from db import db
from flask_migrate import Migrate
import logging
from logging.handlers import TimedRotatingFileHandler
import os
from controllers.departments_controller import departments_blueprint
from controllers.jobs_controller import jobs_blueprint
from controllers.employees_controller import employees_blueprint

app = Flask(__name__)
app.config.from_object('test_config.TestConfig')
db.init_app(app)

if not os.path.exists('logs'):
    os.makedirs('logs')

logHandler = TimedRotatingFileHandler(os.path.join('logs', 'test_data_driven_dare.log'),
                                      when='H', interval=1, backupCount=24)
logHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logHandler.setFormatter(formatter)
app.logger.addHandler(logHandler)

migrate = Migrate(app, db)

app.register_blueprint(departments_blueprint, url_prefix='/departments')
app.register_blueprint(jobs_blueprint, url_prefix='/jobs')
app.register_blueprint(employees_blueprint, url_prefix='/employees')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
