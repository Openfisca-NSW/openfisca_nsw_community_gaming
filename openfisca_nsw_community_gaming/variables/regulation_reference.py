import json
from enum import Enum


class PartType(Enum):
    PART = "Part"
    CLAUSE = "Clause"
    SCHEDULE = "Schedule"
    DIVISION = "Division"
    CHAPTER = "Chapter"


class Part(dict):
    def __init__(self, identifier, part_type, title):
        self.part_dict = {
            "identifier": identifier,
            "part_type": part_type,
            "title": title,
            "parts": {}
            }

    def add_part(self, part):
        self.part_dict["parts"][part.part_dict["identifier"]] = part

    def add_parts(self, parts):
        for part in parts:
            self.add_part(part)

    def parts(self):
        return self.part_dict["parts"]

    def __str__(self):
        return json.dumps(self.part_dict, indent=4, sort_keys=True, default=str)

    def __getitem__(self, item):
        return self.part_dict["parts"][item]


class RegulationReference(Part):
    def __init__(self, name, version, commencement):
        self.part_dict = {
            "identifier": name,
            "version": version,
            "commencement": commencement,
            "parts": {}
            }
