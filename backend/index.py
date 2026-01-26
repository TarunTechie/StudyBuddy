from fastapi import FastAPI, UploadFile , File , Depends
from fastapi.responses import FileResponse
from typing import List
from schema import FolderStructure

from fileOps import addFiles , getFolderStructure , removeFiles
app=FastAPI()


@app.get('/')
def hello():
    return {"Server is running"}

@app.post('/uploadFiles')
def uploadFiles(subject:str,files:List[UploadFile]=File(...)):
    return addFiles(subject,files)
    
@app.get('/getFolderStructure')
def getFiles():
    return getFolderStructure()

@app.delete('/delete')
def deleteFiles(folderStructure:FolderStructure=Depends()):
    return removeFiles(folderStructure)