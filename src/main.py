from fastapi import FastAPI
from users import user_routes


app = FastAPI()

app.include_router(user_routes.router)