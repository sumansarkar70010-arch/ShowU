from sqlalchemy.orm import declarative_base

Base = declarative_base()


from app.db.models.user import User
from app.db.models.post import Post
from app.db.models.video import Video
from app.db.models.story import Story
from app.db.models.analytics import Analytics

print("MODELS LOADED")