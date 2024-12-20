from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # hashlib的上下文

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(raw_password, hashed_password):
    return pwd_context.verify(raw_password, hashed_password)