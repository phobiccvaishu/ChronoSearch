from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.datara.routes import router

app = FastAPI(title="ChronoSearch")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/datara/static"), name="static")
templates = Jinja2Templates(directory="app/datara/templates")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "ChronoSearch running successfully 🚀"}
