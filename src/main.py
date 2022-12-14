from fastapi import FastAPI
from users import user_routes
from cameras import camera_routes
from auth import auth_routes


app = FastAPI(
    title="Siscam"
)

app.include_router(user_routes.router)
app.include_router(camera_routes.router)
app.include_router(auth_routes.router)
