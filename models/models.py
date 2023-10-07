from datetime import datetime
from db import db
from .types.custom_types import StringDateTime

class Department(db.Model):
    __tablename__ = 'departments'
    department_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)


class Job(db.Model):
    __tablename__ = 'jobs'
    job_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)


class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    hired_at = db.Column(StringDateTime, default=datetime.now)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'))
