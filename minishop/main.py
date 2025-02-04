import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/{name}")
def top(name):
    return {"name":name, "message": name[::-1]}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)