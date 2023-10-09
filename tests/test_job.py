import unittest
from models.job import Job
from test_main import app, db


class TestJob(unittest.TestCase):

    def setUp(self):
        app.config.from_object('test_config.TestConfig')
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_job_creation(self):
        job = Job(name='Test Job')
        with app.app_context():
            db.session.add(job)
            db.session.commit()
            test_job = Job.query.filter_by(name='Test Job').first()
            self.assertIsNotNone(test_job)


if __name__ == '__main__':
    unittest.main()
