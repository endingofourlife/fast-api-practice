from pydantic import BaseModel


class Software(BaseModel):
    id: int
    name: str
    version: str
    price: float
    description: str
