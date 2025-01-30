import uvicorn
from fastapi import FastAPI, Depends, Header
from models.account import  AccountModelResponse
from resources.account_resource import AccountResource, FileResource
from middlewares.create_token import TokenCreation, oauth2_scheme
from middlewares.token_verification import VerificationToken

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)


@app.get('/')
def homepage():
    return {"Message:": "Welcome, this is an account register API :D "}


@app.get('/accounts')
def list_account(token: str = Depends(oauth2_scheme), uid_header: str = Header(...)):
    route_security = VerificationToken()
    auth_token = route_security.verify_token(token, uid_header)

    view_account = AccountResource()
    result = view_account.list_accounts()
    return result


@app.get('/accounts/{name}')
def view_account_by_name(name: str, token: str = Depends(oauth2_scheme), uid_header: str = Header(...)):
    route_security = VerificationToken()
    auth_token = route_security.verify_token(token, uid_header)

    view_acc_name = AccountResource()
    result = view_acc_name.list_acc_name(name)
    return result


@app.post('/accounts/register')
def register_file_db(token: str = Depends(oauth2_scheme), uid_header: str = Header(...)):
    route_security = VerificationToken()
    auth_token = route_security.verify_token(token, uid_header)
    
    add_file_db = FileResource()
    result = add_file_db.register_file()
    return result


@app.post('/accounts/register/new', response_model=AccountModelResponse)
def new_account(account: AccountModelResponse, token: str = Depends(oauth2_scheme), uid_header: str = Header(...)):
    route_security = VerificationToken()
    auth_token = route_security.verify_token(token, uid_header)
    
    account_resource = AccountResource()
    result = account_resource.new_account(account)
    return AccountModelResponse(name=account.name, number=account.number)


@app.put('/accounts/update/{id_account}', response_model=AccountModelResponse)
def update_account(id_account: int, account: AccountModelResponse, token: str = Depends(oauth2_scheme), uid_header: str = Header(...)):
    route_security = VerificationToken()
    auth_token = route_security.verify_token(token, uid_header)
    
    account_resource = AccountResource()
    result = account_resource.update_account(id_account, account)
    return AccountModelResponse(name=account.name, number=account.number)


@app.delete('/accounts/delete/{id_account}')
def del_account(id_account: int, token: str = Depends(oauth2_scheme), uid_header: str = Header(...)):
    route_security = VerificationToken()
    auth_token = route_security.verify_token(token, uid_header)
    
    account_resource = AccountResource()
    result = account_resource.delete_account(id_account)
    return {"message": "Account deleted successfully"}


@app.post('/token')
def authorization_token():
    token_middleware = TokenCreation()
    result = token_middleware.create_access_token()

    return result

# Test Route
@app.get('/safety')
def test_safety(token: str = Depends(oauth2_scheme), uid_header: str = Header(...)):
    token_user = VerificationToken()
    result = token_user.verify_token(token, uid_header)

    return {"Message": "Access successfull"}
