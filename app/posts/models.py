from app.posts.schemas import PostSchema


# For db models
class PostDB(PostSchema):
    id: int
