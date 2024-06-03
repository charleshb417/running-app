from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.database import engine
from app.dependencies import get_templates
from app.models import Base
from app.routers import workouts

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(workouts.router)


@app.get("/", response_class=HTMLResponse)
async def read_root(
    request: Request, templates: Jinja2Templates = Depends(get_templates)
):
    return templates.TemplateResponse("index.html", {"request": request})
