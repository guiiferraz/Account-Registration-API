import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
import pytest
from src.app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def testclient():
    client = TestClient(app) 
    
    response = client.post('/token')
    token = response.json().get('token')

    client.headers = {
        "Authorization": f'Bearer {token}',
        "uid-header": "a31755cd-66df-4a84-a747-02b1de760708"
    }
    
    return client


@pytest.fixture(scope='function')
def session():
    DB_URL_TEST = os.getenv('DB_URL_TEST')
    engine = create_engine(DB_URL_TEST)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.begin()

    yield session

    session.rollback()
    session.close()


@pytest.fixture
def account():
    return {
        'id': 1,
        'name': 'testuser',
        'number': 123
    }    
