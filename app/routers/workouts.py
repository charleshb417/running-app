from datetime import datetime

from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.dependencies import get_db, get_templates
from app.repositories import WorkoutRepository
from app.schemas import Workout, WorkoutCreate, WorkoutUpdate

router = APIRouter(
    prefix="/workouts",
    tags=["workouts"],
    dependencies=[Depends(get_db), Depends(get_templates)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Workout)
def create_workout(
    request: Request,
    timestamp: datetime = Form(...),
    run_type: str = Form(...),
    distance_in_mi: float = Form(...),
    duration_in_ms: int = Form(...),
    avg_heart_rate: int = Form(...),
    db: Session = Depends(get_db),
    templates: Jinja2Templates = Depends(get_templates),
):
    workout_data = WorkoutCreate(
        timestamp=timestamp,
        run_type=run_type,
        distance_in_mi=distance_in_mi,
        duration_in_ms=duration_in_ms,
        avg_heart_rate=avg_heart_rate,
    )

    new_workout = WorkoutRepository(db).create(workout_data)

    accept = request.headers.get("accept")
    if "text/html" in accept:
        return templates.TemplateResponse(
            "workouts.html", {"request": request, "workouts": [new_workout]}
        )

    return new_workout


@router.get("/{workout_id}", response_model=Workout)
def read_workout(workout_id: int, db: Session = Depends(get_db)):
    db_user = WorkoutRepository(db).get(workout_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return db_user


@router.get("/", response_model=list[Workout])
async def list_workouts(
    request: Request,
    db: Session = Depends(get_db),
    templates: Jinja2Templates = Depends(get_templates),
):
    workouts = WorkoutRepository(db).list()

    accept = request.headers.get("accept")
    if "text/html" in accept:
        return templates.TemplateResponse(
            "workouts.html", {"request": request, "workouts": workouts}
        )

    return workouts


@router.put("/{workout_id}", response_model=Workout)
def update_workout(
    workout_id: int, workout: WorkoutUpdate, db: Session = Depends(get_db)
):
    return WorkoutRepository(db).update(workout_id, workout)


@router.delete("/{workout_id}", status_code=204)
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    WorkoutRepository(db).delete(workout_id)
