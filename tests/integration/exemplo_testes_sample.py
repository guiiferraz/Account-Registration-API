import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

import pytest
from app import app
from utils.utils import FileHandler
from models.db_connector import db_session
from fastapi.testclient import TestClient

client = TestClient(app)

# Utilizar Fixtures tanto para a conexão com o banco, quanto para valores/estruturas que reutilizarei (WIP)
def test_connection_with_database():
    try:
        session = db_session()
        return session
    
    except Exception as e:
        pytest.fail(f'Connection error with database: {e}')


def test_db_connection():
    assert test_connection_with_database is not None


class TestShowingAccounts:
    def test_homepage_returning_a_message_of_welcome(self):

        response = client.get('/')

        assert response.status_code == 200

        assert response.json() == {"Message:": "Welcome, this is an account register API :D "}


    def test_showing_a_list_of_accounts_in_json(self):
        response = client.get('/accounts')

        assert response.status_code == 200

        data = response.json() 
        assert isinstance(data, list)

        for accounts in data:
            assert isinstance(accounts, dict)
            assert 'id' in accounts
            assert 'name' in accounts
            assert 'number' in accounts


    def test_showing_the_respective_account_by_name(self):
        name = 'Ichigo'

        response = client.get(f'/accounts/{name}')

        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, list)

        for accounts in data:
            assert isinstance(accounts, dict)
            assert 'id' in accounts
            assert accounts['name'] == name
            assert 'number' in accounts


class TestCreateAccounts:
    def test_register_excel_to_database(self):
        file = FileHandler().read_excel()
        accounts_list = list()

        for row in file.itertuples():
            account_data = {
                'name': row.Nome,
                'number': row.Numero
            }

            accounts_list.append(account_data)

        response = client.post('/accounts/register', json=accounts_list)

        assert response.status_code == 200

        assert response.json() == {"Message:": "Accounts registered in database with susscessfully!"}


    def test_new_account_response(self):
        account_data = {
            'name': 'sample',
            'number': 9999
        }

        response = client.post('/accounts/register/new', json=account_data)

        assert response.status_code == 200

        data = response.json()
        assert data['name'] == 'sample'
        assert data['number'] == 9999


class TestUpdateAccount:
    def test_update_account_valus(self):
        id_account = 1
        account_data = {
            'name': 'test',
            'number': 8888
        }

        response = client.put(f'/accounts/update/{id_account}', json=account_data)
        assert response.status_code == 200

        data = response.json()
        assert data['name'] == account_data['name']
        assert data['number'] == account_data['number']


class TestDeleteAccount:
    def test_delete_existing_account(self):
        id_account = 1

        response = client.delete(f'/accounts/delete/{id_account}')

        assert response.status_code == 200

        assert response.json() == {"message": "Account deleted successfully"}

