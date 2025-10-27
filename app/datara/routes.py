from fastapi import APIRouter, UploadFile, Form
import pandas as pd
from app.datara.search_engine import search_data

router = APIRouter()

data_storage = {}  # folder_name -> DataFrame

@router.post("/upload")
async def upload_csv(file: UploadFile):
    df = pd.read_csv(file.file)
    data_storage[file.filename] = df
    return {"message": f"{file.filename} uploaded successfully", "rows": len(df)}

@router.get("/search")
async def search(q: str, filename: str):
    if filename not in data_storage:
        return {"error": "File not found"}
    df = data_storage[filename]
    results = search_data(df, q)
    return {"results": results[:10]}
