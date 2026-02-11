from pydantic import BaseModel

class JobRequest(BaseModel):
    title: str
    description: str

class JobResponse(BaseModel):
    id: int
    title: str
    description: str
