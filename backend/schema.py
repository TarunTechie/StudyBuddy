from pydantic import BaseModel

root_path='./testing/files/'

class FolderStructure(BaseModel):
    folderName:str
    fileName:str | None=None