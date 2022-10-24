from passlib.context import CryptContext
Crypto_context= CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash(password: str):
    return Crypto_context.hash(password)
def verify(attemptive, actual_password):
    return Crypto_context.verify(attemptive, actual_password)