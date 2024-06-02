from pydantic import BaseModel

class WorkoutBase(BaseModel):
    run_type: str
    distance_in_mi: float
    duration_in_ms: int
    avg_heart_rate: int | None = None

class WorkoutCreate(WorkoutBase):
    pass

class Workout(WorkoutBase):
    id: int

    class Config:
        orm_mode = True