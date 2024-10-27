from typing import List

from fastapi import APIRouter, HTTPException
from models.software import Software
from services.software_service import SoftwareService

router = APIRouter()


@router.get("/software", response_model=List[Software])
def get_all_software():
    return SoftwareService.read_all()


@router.post("/software", response_model=Software)
def add_software(software: Software):
    SoftwareService.create(software)
    return software


@router.put("/software/{software_id}", response_model=Software)
def update_software(software_id: int, software: Software):
    SoftwareService.update(software_id, software)
    return software


@router.delete("/software/{software_id}")
def delete_software(software_id: int):
    SoftwareService.delete(software_id)
    return {"message": "Software deleted successfully"}
