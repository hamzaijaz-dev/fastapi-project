from datetime import datetime as dt

from app.database import database, posts
from app.posts.models import PostSchema


# Service for business logic
async def post(payload: PostSchema):
    created_at = dt.now().strftime("%Y-%m-%d %H:%M")
    query = posts.insert().values(title=payload.title, content=payload.content, created_at=created_at)
    return await database.execute(query=query)


async def get(id: int):
    query = posts.select().where(posts.c.id == id)
    return await database.fetch_one(query=query)


async def get_all():
    query = posts.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: PostSchema = None):
    query = (
        posts.update()
        .where(posts.c.id == id)
        .values(
            title=payload.title,
            content=payload.content,
        )
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = posts.delete().where(id == posts.c.id)
    return await database.execute(query=query)
