import uvicorn
from fastapi import FastAPI
from users import users_views
from items import items_views


app = FastAPI()
app.include_router(users_views.router, tags=["Users"])
app.include_router(items_views.router, tags=["Items"])


@app.get("/")
def name():
    return "hello"

#коммент в фиче
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)