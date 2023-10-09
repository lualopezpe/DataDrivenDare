class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Test.db'  # Use an in-memory SQLite database for testing
    SQLALCHEMY_TRACK_MODIFICATIONS = False
