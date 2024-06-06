from abc import ABC, abstractmethod
from sqlalchemy import asc
from sqlalchemy.orm import Session

from app import models, schemas


class BaseRepository(ABC):
    def __init__(self, db: Session):
        self.db = db

    @abstractmethod
    def get(self, id: int) -> schemas.BaseModel:
        pass

    @abstractmethod
    def list(self, skip: int = 0, limit: int = 100) -> list[schemas.BaseModel]:
        pass

    @abstractmethod
    def create(self, obj: schemas.BaseModel) -> schemas.BaseModel:
        pass

    @abstractmethod
    def update(self, id: int, obj: schemas.BaseModel) -> schemas.BaseModel:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass


class WorkoutRepository(BaseRepository):
    def get(self, id: int) -> schemas.Workout:
        return self.db.query(models.Workout).filter(models.Workout.id == id).first()

    def list(self, skip: int = 0, limit: int = 100) -> list[schemas.Workout]:
        return (
            self.db.query(models.Workout)
            .order_by(asc(models.Workout.timestamp))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, obj: schemas.WorkoutCreate):
        db_workout = models.Workout(
            run_type=obj.run_type,
            timestamp=obj.timestamp,
            distance_in_mi=obj.distance_in_mi,
            duration_in_ms=obj.duration_in_ms,
            avg_heart_rate=obj.avg_heart_rate,
        )
        self.db.add(db_workout)
        self.db.commit()
        self.db.refresh(db_workout)
        return db_workout

    def update(self, id: int, obj):
        db_workout = self.get(id)
        if db_workout:
            for attr, value in obj.dict(exclude_unset=True).items():
                setattr(db_workout, attr, value)
            self.db.commit()
            self.db.refresh(db_workout)
            return db_workout

    def delete(self, id: int):
        workout = self.get(id)
        if workout:
            self.db.delete(workout)
            self.db.commit()
