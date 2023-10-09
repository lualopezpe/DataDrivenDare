import unittest
from models.employee import Employee
from models.department import Department
from models.job import Job
from test_main import app, db


class TestEmployee(unittest.TestCase):

    def setUp(self):
        app.config.from_object('test_config.TestConfig')
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_department_creation(self):
        job = Job(name='Test Job')
        department = Department(name='Test Department')

        with app.app_context():
            db.session.add(job)
            db.session.add(department)
            test_job = Job.query.filter_by(name='Test Job').first()
            test_department = Department.query.filter_by(name='Test Department').first()
            employee = Employee(name='Test Employee', department_id=test_department.department_id, job_id=test_job.job_id)
            db.session.add(employee)
            db.session.commit()
            test_employee = Employee.query.filter_by(name='Test Employee').first()
            self.assertIsNotNone(test_employee)


if __name__ == '__main__':
    unittest.main()
