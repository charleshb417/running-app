from fastapi import APIRouter

router = APIRouter(
    prefix='/workouts',
    tags=['workouts'],
    responses={404: {'description': 'Not found'}}
)

@router.get('/')
async def read_workouts():
    return {'data':[]}