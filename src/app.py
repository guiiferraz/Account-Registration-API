import uvicorn
from fastapi import FastAPI
from models.account import  AccountModelResponse
from resources.account_resource import AccountResource, FileResource

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)


@app.get('/')
def homepage():
    return {"Message:": "Welcome, this is an account register API :D "}


@app.get('/accounts')
def list_account():
    view_account = AccountResource()
    result = view_account.list_accounts()
    return result


@app.get('/accounts/{name}')
def view_account_by_name(name: str):
    view_acc_name = AccountResource()
    result = view_acc_name.list_acc_name(name)
    return result


@app.post('/accounts/register')
def register_file_db():
    add_file_db = FileResource()
    result = add_file_db.register_file()

    return {"Message:": "Accounts registered in database with susscessfully!"}


@app.post('/accounts/register/new', response_model=AccountModelResponse)
def new_account(account: AccountModelResponse):
    account_resource = AccountResource()
    result = account_resource.new_account(account)

    return AccountModelResponse(name=account.name, number=account.number)


@app.put('/accounts/update/{id_account}', response_model=AccountModelResponse)
def update_account(id_account: int, account: AccountModelResponse):
    account_resource = AccountResource()
    result = account_resource.update_account(id_account, account)

    return AccountModelResponse(name=account.name, number=account.number)


@app.delete('/accounts/delete/{id_account}')
def del_account(id_account: int):
    account_resource = AccountResource()
    result = account_resource.delete_account(id_account)

    return {"message": "Account deleted successfully"}
