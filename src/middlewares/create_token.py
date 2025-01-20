import os
import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from zoneinfo import ZoneInfo

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXP_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

class TokenCreation:
    def __init__(self):
        pass

    def create_access_token(self):
        expires_in = datetime.now(tz=ZoneInfo("UTC")) + timedelta(minutes=ACCESS_TOKEN_EXP_MINUTES)
        payload = {
            "uid": "a31755cd-66df-4a84-a747-02b1de760708",
            "exp": expires_in
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return {"token": token}
