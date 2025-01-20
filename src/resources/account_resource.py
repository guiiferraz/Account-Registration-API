from controllers.account_controller import AccountController, FileController
from models.account import AccountModelResponse

class AccountResource:
    def __init__(self):
        pass


    def list_accounts(self):
        view_account = AccountController()
        result = view_account.list_accounts()
        return result
    

    def list_acc_name(self, name: str):
        view_acc_name = AccountController()
        result = view_acc_name.list_accounts_name(name)
        return result

    
    def new_account(self, account: AccountModelResponse):
        controller = AccountController()
        result = controller.new_account(account)
        return result


    def update_account(self, id_account, account: AccountModelResponse):
        controller = AccountController()
        result = controller.update_account(id_account, account)
        return result


    def delete_account(self, id_account: int):
        controller = AccountController()
        result = controller.delete_acount(id_account)
        return result


class FileResource:
    def __init__(self):
        pass


    def register_file(self):
        add_xlsx_db = FileController
        result = add_xlsx_db.register_xlsx(self)
        return result
