import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/{name}")
def top_name(name):
    return {"name":name, "message": name[::-1]}

@app.get("/")
def name():
    return "hello"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)