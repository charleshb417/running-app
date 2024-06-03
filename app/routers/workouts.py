from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.repositories import WorkoutRepository
from app.schemas import Workout, WorkoutCreate

router = APIRouter(
    prefix="/workouts",
    tags=["workouts"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[Workout])
async def list_workouts(db: Session = Depends(get_db)):
    workouts = WorkoutRepository(db).list()
    return workouts


@router.post("/", response_model=Workout)
def create_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
    return WorkoutRepository(db).create(workout)
