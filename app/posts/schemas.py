from datetime import datetime as dt

from pydantic import BaseModel, Field
from pydantic.schema import datetime
from pytz import timezone as tz


# Define schema for pydantic models and validation purpose
class PostSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    content: str = Field(..., min_length=3, max_length=50)
    created_at: datetime = dt.now(tz("UTC")).strftime("%Y-%m-%d %H:%M")
