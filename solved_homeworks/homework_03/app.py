from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/ping")
def view():
    return {"message": "pong"}