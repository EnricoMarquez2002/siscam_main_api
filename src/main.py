from fastapi import FastAPI
from users import user_routes
from cameras import camera_routes


app = FastAPI()

app.include_router(user_routes.router)
app.include_router(camera_routes.router)