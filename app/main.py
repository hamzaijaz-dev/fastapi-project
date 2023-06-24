from app.database import database, engine, metadata
from app.posts import router
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

metadata.create_all(engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(router.router, prefix="/posts", tags=["posts"])
