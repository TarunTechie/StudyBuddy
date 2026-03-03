from fastapi import FastAPI
from fileOps import router as fileRouter
from dbOps import router as dbRouter
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(fileRouter)
app.include_router(dbRouter)

@app.get('/')
def hello():
    return {"Server is running"}