from db import db


class Department(db.Model):
    __tablename__ = 'departments'
    __table_args__ = {'extend_existing': True}
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
