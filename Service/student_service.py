from typing import List

from Domain.nota import Nota
from Domain.notavalidator import NotaValidator
from Domain.student import Student
from Domain.studentvalidator import StudentValidator
from Repository.repository import Repository


class StudentService:
    def __init__(self,
                 student_repository: Repository,
                 student_validator: StudentValidator):
        '''

        :param student_repository:repository student
        :param student_validator: validator pt student
        '''
        self.student_repository = student_repository
        self.student_validator = student_validator

    def add_student(self,
                    id_student: str,
                    nume: str,
                    anul: int,
                    tip_bursa: str):
        '''
        Se adauga un student
        :param self:
        :param id_student:id-ul studentului
        :param nume:numele studentului
        :param anul:anul
        :param tip_bursa:tipul bursei
        '''
        student = Student(id_student, nume, anul,
                          tip_bursa)
        self.student_repository.create(student)

    def get_all(self) -> List[Nota]:
        '''
        citeste/afiseaza lista
        :return:nota repository
        '''
        return self.student_repository.read()

    def ordonare_an(self, x: str):
        '''
        Ordonarea descrescatoare dupa an a
         studentilor cu bursa 'x'.
        :param x:tipul de bursa
        :return:studentii ordonati descrescator
                dupa an
        '''
        studenti = self.student_repository.read()
        k = []
        for s in studenti:
            if s.tip_bursa.lower() == x.lower():
                k.append(s)
        return sorted(k, key=lambda y: y.anul, reverse=True)