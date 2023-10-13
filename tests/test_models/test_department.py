import unittest
from models.department import Department
from test_main import app, db


class TestDepartment(unittest.TestCase):

    def setUp(self):
        app.config.from_object('test_config.TestConfig')
        with app.app_context():
            db.create_all()

    def tearDown(self):
        app.config.from_object('test_config.TestConfig')
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_department_creation(self):
        department = Department(name='Test Department')
        with app.app_context():
            db.session.add(department)
            db.session.commit()
            test_department = Department.query.filter_by(name='Test Department').first()
            self.assertIsNotNone(test_department)


if __name__ == '__main__':
    unittest.main()
