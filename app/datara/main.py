from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.datara.routes import router as datara_router

app = FastAPI(title="ChronoSearch - Data Search App")

app.include_router(datara_router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head><title>ChronoSearch</title></head>
    <body style="font-family:Arial;text-align:center;margin-top:40px;">
    <h1>Welcome to ChronoSearch</h1>
    <p>Upload and search your data easily</p>
    <a href="/upload">Go to Dashboard</a>
    </body>
    </html>
    """
