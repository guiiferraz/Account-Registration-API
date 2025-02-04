import sys
sys.path.insert(0, r'c:\Users\Guilherme\Desktop\Faculdade\api_project\src')
from fastapi import HTTPException
from utils.utils import FileHandler
from src.models import AccountModel, AccountModelResponse, db_session
from sqlalchemy import select, update

class AccountConnector:
    def __init__(self):
        pass

    def list_accounts(self):
        accounts_list = list()

        with db_session() as session:
            stmt = select(AccountModel)

            for accounts in session.scalars(stmt):
                payload = dict()
                payload["id"] = accounts.id
                payload["name"] = accounts.Name
                payload["number"] = accounts.Number

                accounts_list.append(payload)

            return accounts_list

    def list_acc_name(self, name: str):
        accounts_list = list()

        with db_session() as session:
            stmt = select(AccountModel).where(AccountModel.Name == name)

            for account in session.scalars(stmt):
                payload = dict()
                payload["id"] = account.id
                payload["name"] = account.Name
                payload["number"] = account.Number

                accounts_list.append(payload)

            return accounts_list

    def new_account(self, account: AccountModelResponse):
        new_acc = AccountModel(Name=account.name, Number=account.number)

        with db_session() as session:
            session.add(new_acc)
            session.commit()
            session.refresh(new_acc)

        return AccountModelResponse(name=new_acc.Name, number=new_acc.Number)

    def update_account(self, id_account: int, account: AccountModelResponse):
        with db_session() as session:
            stmt = select(AccountModel).filter(AccountModel.id == id_account)
            result = session.execute(stmt).fetchone()

            if not result:
                raise HTTPException(
                    status_code=404, detail="Account not found")

            update_values = {}
            update_values['Name'] = account.name
            update_values['Number'] = account.number

            update_stmt = (update(AccountModel).where(AccountModel.id == id_account)
                           .values(update_values))

            session.execute(update_stmt)
            session.commit()

            return AccountModelResponse(name=account.name, number=account.number)

    def delete_account(self, id_account: int):
        with db_session() as session:
            stmt = select(AccountModel).where(AccountModel.id == id_account)
            result = session.scalars(stmt).one()

            session.delete(result)
            session.commit()


class FileConnector:
    def __init__(self):
        pass

    def xlsx_to_db(self):
        data = FileHandler()
        data.read_excel()

        with db_session() as session:
            accounts_list = list()

            for row in data.read_excel().itertuples():
                new_account = AccountModel(Name=row.Nome, Number=row.Numero)
                
                account = dict()
                account['name'] = new_account.Name
                account['number'] = new_account.Number

                accounts_list.append(account)

                session.add(new_account)
                session.commit()

            return accounts_list
