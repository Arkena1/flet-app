from pydantic import BaseModel
from typing import Optional


class Province(BaseModel):
    id: Optional[int]
    name: str
    
    class Config:
        orm_mode = True

class SubProvince(BaseModel):
    id: Optional[int]
    name: str
    province_id: int
    class Config:
        orm_mode = True

class Area(BaseModel):
    id: Optional[int]
    name: str
    sub_provinces_id: int
    class Config:
        orm_mode = True

class Field(BaseModel):
    id: Optional[int]
    name: str
    areas_id: int
    class Config:
        orm_mode = True

class Pipe(BaseModel):
    id = Optional[int]
    name: str
    fields_id: int
    class Config:
        orm_mode = True

class Source(BaseModel):
    id = Optional[int]
    name: str

    class Config:
        orm_mode = True

class PipeInfo(BaseModel):
    id = Optional[int]
    nitro_total: str
    nitro_a: str
    nitro_b: str
    nitro_percent: str
    platelets: str
    hydrogen: str
    pipes_id: int
    source_id: int
    class Config:
        orm_mode = True
        