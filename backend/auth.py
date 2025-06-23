from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from jose import jwt
from passlib.context import CryptContext
import os, json
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()

USERS_FILE = "users.json"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

class AuthRequest(BaseModel):
    username: str
    password: str

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

@router.post("/signup")
def signup(data: AuthRequest):
    users = load_users()
    if data.username in users:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed = pwd_context.hash(data.password)
    users[data.username] = {"password": hashed}
    save_users(users)

    return {"detail": "User registered successfully"}

@router.post("/login")
def login(data: AuthRequest):
    users = load_users()
    if data.username not in users:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not pwd_context.verify(data.password, users[data.username]["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": data.username, "exp": expire}
    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": access_token, "token_type": "bearer"}
