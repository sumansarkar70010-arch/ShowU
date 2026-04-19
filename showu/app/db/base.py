from sqlalchemy.orm import declarative_base

Base = declarative_base()


from showu.app.db.models.user import User
from showu.app.db.models.post import Post
from showu.app.db.models.video import Video
from showu.app.db.models.story import Story
from showu.app.db.models.analytics import Analytics

print("MODELS LOADED")
