import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
import pytest
from src.app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from src.models.account import AccountModel, AccountModelResponse


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


@pytest.fixture()
def account_setup():
    account = AccountModel(
        Name='test',
        Number=123
    )

    return account


@pytest.fixture()
def account_pydantic():
    account = AccountModelResponse(
        name='testee',
        number=123
    )

    return account


def test_homepage_returning_a_welcome_message(testclient):
    # Arrange:

    # Act:
    response = testclient.get('/')

    # Assert:
    assert response.status_code == 200
    assert response.json() == {"Message:": "Welcome, this is an account register API :D "}


def test_returning_a_list_of_all_accounts_in_database(testclient):
    # Arrange:

    # Act:
    response = testclient.get('/accounts')
    data = response.json()

    # Assert:
    assert response.status_code == 200
    assert isinstance(data, list)


def test_returnin_a_list_with_the_respective_account_name(testclient, session, account_setup):
    # Arrange/SetUp:
    new_account = account_setup
    session.add(new_account)

    # Act:
    response = testclient.get('/accounts/{name}')
    data = response.json()

    # Assert:
    assert response.status_code == 200
    assert isinstance(data, list)

    for account in data:
        assert isinstance(account, dict)
        assert account['name'] == new_account.Name
        assert 'number' in account


def test_returning_a_successfull_list_when_register_all_accounts_file_in_database(testclient, session):
    # Arrange:

    # Act:
    response = testclient.post('/accounts/register')
    data = response.json()

    # Assert:
    assert response.status_code == 200
    assert isinstance(data, list)

    for account in data:
        assert isinstance(account, dict)
        assert 'name' in account
        assert 'number' in account

        assert isinstance(account['name'], str)
        assert isinstance(account['number'], int)

    # Teardown: 
        session.query(AccountModel).filter(AccountModel.Name == account['name']).delete(synchronize_session=False)
        session.commit()


def test_returning_the_respective_account_if_registered_in_database(testclient, account_pydantic, session):
    # Arrange:
    new_account = account_pydantic.model_dump()

    # Act:
    response = testclient.post('/accounts/register/new', json=new_account)
    data = response.json()

    # Assert: 
    assert response.status_code == 200

    assert isinstance(data, dict)
    assert 'name' in data
    assert 'number' in data

    assert isinstance(data['name'], str)
    assert isinstance(data['number'], int)
    
    # Teardown:
    session.query(AccountModel).filter(AccountModel.Name == new_account['name']).delete(synchronize_session=False)
    session.commit()


def test_returning_account_payload_when_the_update_data_is_successfully(testclient, session, account_pydantic, account_setup):
    # Arrange:
    new_account = account_setup
    session.add(new_account)
    session.commit()

    id_account = new_account.id

    update_account = account_pydantic.model_dump()

    # Act:
    response = testclient.put(f'/accounts/update/{id_account}', json=update_account)
    data = response.json()

    # Assert:
    assert response.status_code == 200

    assert isinstance(data, dict)
    assert 'name' in data
    assert 'number' in data
    
    assert isinstance(data['name'], str)
    assert isinstance(data['number'], int)
    
    # Teardown:
    session.query(AccountModel).filter(AccountModel.id == id_account).delete(synchronize_session=False)
    session.commit()


def test_returning_a_successfull_message_if_the_account_was_deleted(testclient, session, account_pydantic, account_setup):
    # Arrante:
    ...
    
    # Act:
    ...

    # Assert:
    ...

    # Teardown:
    ...
