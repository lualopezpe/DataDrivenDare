from datetime import datetime
from db import db
from .types.custom_types import StringDateTime


class Employee(db.Model):
    __tablename__ = 'employees'
    __table_args__ = {'extend_existing': True}
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    hired_at = db.Column(StringDateTime, default=datetime.now)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'))
