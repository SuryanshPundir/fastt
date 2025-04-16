from datetime import datetime, timedelta, timezone
from socialapi.database import user_table, database
from jose import jwt
from fastapi import HTTPException, status
from passlib.context import CryptContext

SECRET_KEY= "q80bqvc9348bfq267b5eeqijf"
ALGORITHM="HS256"
pwd_context = CryptContext(schemes=["bcrypt"])

credentials_exception=HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
)

def create_access_token(email:str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    jwt_data={"sub": email, "exp": expire}
    encoded_jwt = jwt.encode(jwt_data, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def get_user(email: str):
    query= user_table.select().where(user_table.c.email == email)
    result= await database.fetch_one(query)
    if result:
        return result
    

async def authenticate_user(email:str, password:str):
    user= await get_user(email)
    if not user:
        raise credentials_exception
    if not verify_password(password, user.password):
        raise credentials_exception
    return user