from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def frontend():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/")
def home():
    return {"status": "Backend running"}
