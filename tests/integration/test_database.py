import os
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()

DB_URL_TEST = os.getenv('DB_URL_TEST')

def connection_database():
    engine = create_engine(DB_URL_TEST)
    try:
        with Session(engine) as session:
            session.execute(text('SELECT 1'))

            return session
        
    except Exception as e:
        pytest.fail(f'Error with connection: {e}')


def test_connection_tests_database():
    assert connection_database is not None
