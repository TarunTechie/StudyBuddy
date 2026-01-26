from pydantic import BaseModel

class FolderStructure(BaseModel):
    folderName:str
    fileName:str | None=None