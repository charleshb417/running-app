from sqlalchemy import Column, Date, Float, Integer, String

from app.database import Base


class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    run_type = Column(String)
    timestamp = Column(Date)
    distance_in_mi = Column(Float)
    duration_in_ms = Column(Integer)
    avg_heart_rate = Column(Integer, nullable=True)
