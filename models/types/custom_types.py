from sqlalchemy.types import TypeDecorator, DateTime
from datetime import datetime
from dateutil.parser import parse


class StringDateTime(TypeDecorator):
    impl = DateTime

    def process_bind_param(self, value, dialect):
        if value is not None:
            return datetime.fromisoformat(parse(value))
            # return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            # return value.strftime('%Y-%m-%d %H:%M:%S')
            return value.isoformat()
        return value
