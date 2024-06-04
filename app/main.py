from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import engine
from app.dependencies import get_db, get_templates
from app.models import Base
from app.repositories import WorkoutRepository
from app.routers import workouts

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(workouts.router)


@app.get("/", response_class=HTMLResponse)
async def read_root(
    request: Request,
    templates: Jinja2Templates = Depends(get_templates),
    db: Session = Depends(get_db),
):
    db_workouts = WorkoutRepository(db).list()
    return templates.TemplateResponse(
        "index.html", {"request": request, "workouts": db_workouts}
    )
