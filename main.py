from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base  

app = FastAPI()


Base.metadata.create_all(bind=engine)
from app.api.v1 import auth, users, posts, videos, stories, analytics
from app.db.session import engine 


try:
    from app.db.base import Base
except ImportError:
    try:
        from app.db.base import Base
    except ImportError:
        
        from sqlalchemy.ext.declarative import declarative_base
        Base = declarative_base()

def create_application() -> FastAPI:
    app = FastAPI(title="ShowU Social Media App", version="1.0.0")
    
    app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
    app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
    app.include_router(posts.router, prefix="/api/v1/posts", tags=["Posts"])
    app.include_router(videos.router, prefix="/api/v1/videos", tags=["Videos"])
    app.include_router(stories.router, prefix="/api/v1/stories", tags=["Stories"])
    app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])
    return app

app = create_application()

Base.metadata.create_all(bind=engine)
