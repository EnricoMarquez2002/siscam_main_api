from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from .auth_handler import JWT_ALGORITHM, JWT_SECRET


class JWTBearer(HTTPBearer):
    def __inti__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication scheme")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token or expired token")
            return self.get_user(credentials.credentials)
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authorization code")

    def verify_jwt(self, jwtoken: str):
        valid = False
        try:
            payload = jwt.decode(jwtoken, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except:
            payload = None
        if payload:
            valid = True
        return valid

    def get_user(self, credenciais):
        user = jwt.decode(credenciais, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = user.get("id")
        return user
