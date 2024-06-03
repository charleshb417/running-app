from app.database import SessionLocal
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


def durationformat(value: int) -> str:
    """
    Custom Jinja2 filter to format duration from milliseconds to HH:MM:SS format.
    """
    seconds, milliseconds = divmod(value, 1000)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


templates.env.filters["durationformat"] = durationformat


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_templates():
    return templates
