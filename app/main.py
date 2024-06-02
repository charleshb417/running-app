from fastapi import FastAPI

from app.routers import workouts

app = FastAPI()

app.include_router(workouts.router)