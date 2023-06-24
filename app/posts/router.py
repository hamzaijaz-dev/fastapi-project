from datetime import datetime as dt
from typing import List

from app.posts import service
from app.posts.models import PostDB
from app.posts.schemas import PostSchema
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.post("/", response_model=PostDB, status_code=201)
async def create_post(payload: PostSchema):
    post_id = await service.post(payload)
    created_at = dt.now().strftime("%Y-%m-%d %H:%M")

    response_object = {
        "id": post_id,
        "title": payload.title,
        "content": payload.content,
        "created_at": created_at,
    }
    return response_object


@router.get("/{post_id}/", response_model=PostDB)
async def read_post(
    post_id: int = Path(..., gt=0),
):
    post = await service.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Note not found")
    return post


@router.get("/", response_model=List[PostDB])
async def read_all_posts():
    return await service.get_all()


@router.put("/{post_id}/", response_model=PostDB)
async def update_post(payload: PostSchema, post_id: int = Path(..., gt=0)):
    post = await service.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Note not found")
    post_id = await service.put(post_id, payload)
    response_object = {
        "id": post_id,
        "title": payload.title,
        "content": payload.content,
    }
    return response_object


@router.delete("/{post_id}/", response_model=PostDB)
async def delete_post(post_id: int = Path(..., gt=0)):
    post = await service.get(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Note not found")
    await service.delete(post_id)

    return post
