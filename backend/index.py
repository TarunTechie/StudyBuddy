from fastapi import FastAPI
from fileOps import router as fileRouter
from dbOps import router as dbRouter

app=FastAPI()
app.include_router(fileRouter)
app.include_router(dbRouter)

@app.get('/')
def hello():
    return {"Server is running"}