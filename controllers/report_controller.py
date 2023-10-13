from flask import Blueprint, request, jsonify
from sqlalchemy import func, extract, case
from db import db
from models.department import Department
from models.employee import Employee
from models.job import Job

reports_blueprint = Blueprint('reports', __name__)


@reports_blueprint.route('/report1', methods=['GET'])
def get_report1():
    year = int(request.args.get('year', 2021))

    results = db.session.query(
        Department.department_id,
        Job.job_id,
        func.count(case([(extract('quarter', Employee.hired_at) == 1, Employee.employee_id)])).label('Q1'),
        func.count(case([(extract('quarter', Employee.hired_at) == 2, Employee.employee_id)])).label('Q2'),
        func.count(case([(extract('quarter', Employee.hired_at) == 3, Employee.employee_id)])).label('Q3'),
        func.count(case([(extract('quarter', Employee.hired_at) == 4, Employee.employee_id)])).label('Q4'),
        func.count(Employee.employee_id).label('employee_count')
    ).join(Employee, Employee.department_id == Department.department_id) \
        .join(Job, Job.job_id == Employee.job_id) \
        .filter(extract('year', Employee.hired_at) == year) \
        .group_by(Department.department_id, Job.job_id, extract('quarter', Employee.hired_at)) \
        .order_by(Department.department_id, Job.job_id, extract('quarter', Employee.hired_at)) \
        .all()

    return jsonify([dict(row) for row in results])


@reports_blueprint.route('/report2', methods=['GET'])
def get_report2():
    year = int(request.args.get('year', 2021))

    count_hires = db.session.query(
        Department.department_id,
        func.count(Employee.employee_id).label('count_per_department')) \
        .join(Employee, Employee.department_id == Department.department_id) \
        .filter(extract('year', Employee.hired_at) == year) \
        .group_by(Department.department_id) \
        .subquery()

    mean_hires = db.session.query(
        func.avg(count_hires.c.count_per_department)
    ).scalar()

    # Query for departments hiring above the mean
    results = db.session.query(
        Department.department_id,
        Department.name,
        func.count(Employee.employee_id).label('number_of_employees')
    ).join(Employee, Employee.department_id == Department.department_id) \
        .filter(extract('year', Employee.hired_at) == year) \
        .group_by(Department.department_id, Department.name) \
        .having(func.count(Employee.department_id) > mean_hires) \
        .order_by(func.count(Employee.employee_id).desc()) \
        .all()

    return jsonify([dict(row) for row in results])


@reports_blueprint.route('/report3', methods=['GET'])
def get_reports3():
    year = int(request.args.get('year', 2021))
    results = db.session.execute(f"""
        SELECT 
        d.department_id, 
        j.job_id,
        COUNT(CASE WHEN EXTRACT(quarter FROM he.hired_at) = 1 THEN 1 END) AS Q1,
        COUNT(CASE WHEN EXTRACT(quarter FROM he.hired_at) = 2 THEN 1 END) AS Q2,
        COUNT(CASE WHEN EXTRACT(quarter FROM he.hired_at) = 3 THEN 1 END) AS Q3,
        COUNT(CASE WHEN EXTRACT(quarter FROM he.hired_at) = 4 THEN 1 END) AS Q4
        FROM employees he
        INNER JOIN departments d ON d.department_id = he.department_id 
        INNER JOIN jobs j ON j.job_id = he.job_id 
        WHERE EXTRACT(year FROM he.hired_at) = {year}
        GROUP BY d.department_id, j.job_id
        ORDER BY d.department_id ASC, j.job_id ASC;
    """)

    return jsonify([dict(row) for row in results])


@reports_blueprint.route('/report4', methods=['GET'])
def get_reports4():
    year = int(request.args.get('year', 2021))
    results = db.session.execute(f"""
        WITH department_hires AS (
            SELECT he.department_id, COUNT(*) AS hire_count
            FROM employees he
            WHERE EXTRACT(year FROM he.hired_at) = {year}
            GROUP BY department_id
        ),
        department_avg AS (
            SELECT AVG(hire_count) AS avg_hires
            FROM department_hires
        )
        SELECT 
            d.department_id , 
            d.name, 
            dh.hire_count AS hired
        FROM departments d
        INNER JOIN department_hires dh ON dh.department_id = d.department_id 
        WHERE dh.hire_count > (SELECT avg_hires FROM department_avg)
        ORDER BY dh.hire_count DESC;
    """)

    return jsonify([dict(row) for row in results])
