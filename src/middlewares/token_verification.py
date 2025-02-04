import jwt
from fastapi import HTTPException, Header
from src.middlewares.create_token import SECRET_KEY, ALGORITHM

class VerificationToken:
    def __init__(self):
        pass
    
    def verify_token(self, token: str, uid_header: str = Header(...)):
        try:
            
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            uid_token = payload.get("uid")

            if not uid_token or uid_token != uid_header:
                raise HTTPException(
                    status_code=400,
                    detail="Unauthorized: UID does not match"
                )
            return uid_token

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401,
                detail="Expired Token"
            )
        except jwt.InvalidSignatureError:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )
        except jwt.exceptions.DecodeError:
            raise HTTPException(
                status_code=401,
                detail="Cannot decode token"
            )
