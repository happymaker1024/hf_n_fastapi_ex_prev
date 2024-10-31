from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import HTMLResponse
from transformers import pipeline
from contextlib import asynccontextmanager
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn 

ml_model = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
  # Load the ML model
  ml_model["summarizer"] = pipeline("summarization", "sshleifer/distilbart-cnn-12-6", device=0)
  yield
  # Clean up the ML models and release the resources
  ml_model.clear()

templates = Jinja2Templates(directory="templates")
app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static") 

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
  return templates.TemplateResponse("exam10_v1.html", {'request': request})

@app.post("/summarize", response_class=HTMLResponse)
async def summary(request: Request, file: UploadFile):
  content = await file.read()
  content = content.decode()
  content = content.replace('\r\n', '')
  result = ml_model["summarizer"](content)
  summary = f"{result[0]['summary_text']}"

  return templates.TemplateResponse("exam10_v2.html", {"request": request, "summary": summary})

if __name__ == "__main__":
  uvicorn.run("exam10:app", port=8000, host="localhost", reload=True)

