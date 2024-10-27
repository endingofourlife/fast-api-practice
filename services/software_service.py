import json
from models.software import Software
from typing import List


class SoftwareService:
    data_file = "data/software.json"

    @staticmethod
    def read_all() -> List[Software]:
        with open(SoftwareService.data_file, "r") as file:
            data = json.load(file)
            return [Software(**item) for item in data]

    @staticmethod
    def write_all(softwares: List[Software]):
        with open(SoftwareService.data_file, "w") as file:
            json.dump([software.dict() for software in softwares], file)

    @staticmethod
    def create(software: Software):
        softwares = SoftwareService.read_all()
        softwares.append(software)
        SoftwareService.write_all(softwares)

    @staticmethod
    def update(software_id: int, updated_software: Software):
        softwares = SoftwareService.read_all()
        for index, item in enumerate(softwares):
            if item.id == software_id:
                softwares[index] = updated_software
                break
        SoftwareService.write_all(softwares)

    @staticmethod
    def delete(software_id: int):
        softwares = SoftwareService.read_all()
        softwares = [item for item in softwares if item.id != software_id]
        SoftwareService.write_all(softwares)
