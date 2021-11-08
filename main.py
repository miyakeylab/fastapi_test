from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/miyake")
async def root():
    return {"message": "Hello Miyake"}
