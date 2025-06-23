from fastapi import UploadFile, File, Depends, APIRouter, HTTPException, Security
import os, shutil, re, requests
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
security = HTTPBearer()

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid or expired token")
    return token  # optional, but good practice

@router.post("/upload")
def upload_resume(
    file: UploadFile = File(...),
    token: str = Depends(verify_token)  # This enforces token validation
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Upload only PDF files.")

    UPLOAD_DIR = "uploads"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    filename = re.sub(r"[^\w\-.]", "_", file.filename)
    save_path = os.path.join(UPLOAD_DIR, filename)

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if not N8N_WEBHOOK_URL:
        raise HTTPException(status_code=500, detail="N8N_WEBHOOK_URL is not configured.")

    try:
        with open(save_path, "rb") as f:
            response = requests.post(
                N8N_WEBHOOK_URL,
                files={"file": (filename, f, "application/pdf")},
                data={"filename": filename}
            )
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"n8n error: {response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending to n8n: {str(e)}")

    return {"detail": "File uploaded and sent to n8n successfully"}
