from models.account import AccountModelResponse
from connectors.account_connector import AccountConnector, FileConnector

class AccountController:
    def __init__(self):
        pass


    def list_accounts(self):
        view_account = AccountConnector()
        return view_account.list_accounts()


    def list_accounts_name(self, name: str):
        view_acc_name = AccountConnector()
        return view_acc_name.list_acc_name(name)


    def new_account(self, account: AccountModelResponse):
        connector = AccountConnector()
        return connector.new_account(account)
    

    def update_account(self, id_account, account: AccountModelResponse):
        connector = AccountConnector()
        return connector.update_account(id_account, account)


    def delete_acount(self, id_account: int):
        connector = AccountConnector()
        return connector.delete_account(id_account)


class FileController:
    def __init__(self):
        pass


    def register_xlsx(self):
        register_file = FileConnector()
        return register_file.xlsx_to_db()
