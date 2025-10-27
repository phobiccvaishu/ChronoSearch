from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.datara.routes import router as datara_router

app = FastAPI(title="ChronoSearch - Data Search App")

# Mount router
app.include_router(datara_router)

# Mount static directory for CSS, JS, etc.
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Home page
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>ChronoSearch</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="container">
            <h1>Welcome to ChronoSearch</h1>
            <p>Upload and search your data easily</p>
            <a class="btn" href="/upload">Go to Dashboard</a>
        </div>
    </body>
    </html>
    """
