from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Nota(Entity):
    materie: str
    nota: float
    penalizare: float
    id_student: str
