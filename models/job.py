from db import db


class Job(db.Model):
    __tablename__ = 'jobs'
    __table_args__ = {'extend_existing': True}
    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
