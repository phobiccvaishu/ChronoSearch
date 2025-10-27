from fastapi import APIRouter, UploadFile
import pandas as pd
from app.datara.search_engine import search_data

router = APIRouter()

# In-memory storage for uploaded CSVs
data_storage = {}

@router.post("/upload")
async def upload_csv(file: UploadFile):
    """Upload a CSV file and store it temporarily in memory."""
    try:
        df = pd.read_csv(file.file)
        data_storage[file.filename] = df
        return {"message": f"{file.filename} uploaded successfully", "rows": len(df)}
    except Exception as e:
        return {"error": str(e)}

@router.get("/search")
async def search(q: str, filename: str):
    """Search for a keyword within the uploaded CSV."""
    if filename not in data_storage:
        return {"error": "File not found"}
    df = data_storage[filename]
    results = search_data(df, q)
    return {"results": results[:10]}
