from fastapi import FastAPI


app = FastAPI()

@app.get('/root/')
async def hello_world():
    return "Hello World"