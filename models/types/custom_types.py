from sqlalchemy.types import TypeDecorator, DateTime
from datetime import datetime


class StringDateTime(TypeDecorator):
    impl = DateTime

    def process_bind_param(self, value, dialect):
        if value is not None and value != '':
            return datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
        elif value == '':
            return None
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return value.strftime('%Y-%m-%dT%H:%M:%SZ')
        return value
