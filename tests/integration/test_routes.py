import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from src.models.account import AccountModel
from src.models.db_connector import db_session
from sqlalchemy import text


def test_connection_with_database():
    # Arrange:
    session = db_session()

    # Act:
    if session is None:
        print("Error with connection to database!")
        return 
    
    result = session.execute(text("SELECT 1")).scalar()

    # Assert:
    assert result == 1

    # Teardown:
    session.close()


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


def test_returnin_a_list_with_the_respective_account_name(testclient, session, account):
    # Arrange/SetUp:
    new_account = AccountModel(
        id=account['id'], Name=account['name'], Number=account['number']
    )
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


def test_returning_the_respective_account_if_registered_in_database(testclient, session, account):
    # Arrange:

    # Act:
    response = testclient.post('/accounts/register/new', json=account)
    data = response.json()

    # Assert: 
    assert response.status_code == 200

    assert isinstance(data, dict)
    assert 'name' in data
    assert 'number' in data

    assert isinstance(data['name'], str)
    assert isinstance(data['number'], int)
    
    # Teardown:
    session.query(AccountModel).filter(AccountModel.Name == account['name']).delete(synchronize_session=False)
    session.commit()


def test_returning_account_payload_when_the_update_data_is_successfully(testclient, session, account):
    # Arrange:
    new_account = AccountModel(
        id=1, Name='testuser2', Number=321
    )
    session.add(new_account)
    session.commit()

    id_account =new_account.id 

    # Act:
    response = testclient.put(f'/accounts/update/{id_account}', json=account)
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


def test_returning_a_successfull_message_if_the_account_was_deleted(testclient, session, account):
    # Arrange:
    new_account = AccountModel(
        id=account['id'], Name=account['name'], Number=account['number']
    )
    session.add(new_account)
    session.commit()

    id_account = new_account.id
    # Act:
    response = testclient.delete(f'/accounts/delete/{id_account}')
    data = response.json()

    # Assert:
    assert response.status_code == 200
