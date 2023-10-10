import unittest
from test_main import app, db


class TestDepartmentController(unittest.TestCase):

    def setUp(self):
        app.config.from_object('test_config.TestConfig')
        with app.app_context():
            db.create_all()

    def tearDown(self):
        app.config.from_object('test_config.TestConfig')
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_upload_departments(self):
        client = app.test_client()
        with open('data/departments.csv', 'rb') as f:
            response = client.post('departments/upload', data={'file': f})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"departments has been updated successfully!", response.data)

    def test_upload_hist(self):
        client = app.test_client()
        response = client.get('/departments/hist?file_path=data/departments.csv')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"departments has been updated successfully!", response.data)

    def test_file_not_found(self):
        client = app.test_client()
        response = client.get('/departments/hist?file_path=departments.csv')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"File not found!", response.data)

    def test_database_error(self):
        app.config.from_object('test_config.TestConfig')
        with app.app_context():
            db.session.remove()
            db.drop_all()
            client = app.test_client()
            response = client.get('/departments/hist?file_path=data/departments.csv')
            self.assertEqual(response.status_code, 500)
            self.assertIn(b"Database error occurred!", response.data)


if __name__ == '__main__':
    unittest.main()
