from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Student(Entity):
    nume: str
    anul: int
    tip_bursa: str
