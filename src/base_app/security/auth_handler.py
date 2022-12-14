from decouple import config
from base_app.utils.timezone import sp
from typing import Optional
from pydantic import EmailStr
from datetime import datetime, timedelta
from jose import jwt
from auth.repo import AuthRepo


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def create_acess_token(email: EmailStr, user_id: str, expires_delta: Optional[timedelta] = None):
    encode = {"sub": email, "id": user_id}
    if expires_delta:
        expire = datetime.now(tz=sp) + expires_delta
    else:
        expire = datetime.now(tz=sp) + timedelta(minutes=5)
    encode.update({"exp" : expire})
    
    jwtac = jwt.encode(encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    
    AuthRepo.update_acess_token(email, jwtac)
    
    return {
        "token": jwtac,
        "expires": expire,
        "type": "Bearer"
    }