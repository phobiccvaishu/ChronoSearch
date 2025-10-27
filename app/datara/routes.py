from fastapi import APIRouter, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/datara/templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": None, "columns": None})

@router.post("/upload", response_class=HTMLResponse)
async def upload_csv(request: Request, file: UploadFile):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    df = pd.read_csv(file_location)
    data = df.values.tolist()
    columns = df.columns.tolist()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "data": data,
        "columns": columns,
        "filename": file.filename
    })
