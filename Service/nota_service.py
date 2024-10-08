import json
from typing import List

from Domain.nota import Nota
from Domain.notavalidator import NotaValidator
from Domain.student import Student
from Repository.repository import Repository


class NotaService:
    def __init__(self,
                 nota_repository: Repository,
                 nota_validator: NotaValidator,
                 student_repository: Repository):
        '''

        :param nota_repository:repository-ul notei
        :param nota_validator:validatorul
        :param student_repository:repository-ul
        pt student
        '''
        self.nota_repository = nota_repository
        self.nota_validator = nota_validator
        self.student_repository = student_repository

    def add_nota(self,
                 id_nota: str,
                 materie: str,
                 nota: float,
                 penalizare: int,
                 id_student: str):
        '''
        Se adauga o nota.
        :param self:
        :param id_nota:id-ul notei
        :param materie:materia
        :param nota: nota
        :param penalizare: penalizarea
        :param id_student: id-ul studentului
        :return:
        '''
        nota = Nota(id_nota, materie, nota, penalizare, id_student)
        self.nota_validator.validate(nota)
        self.nota_repository.create(nota)

    def get_all(self) -> List[Nota]:
        '''
        citeste/afiseaza lista
        :return:nota repository
        '''
        return self.nota_repository.read()

    def medie_aritmetica(self):
        '''
        Media aritmetica conform cerintei 4.
        :return:
        '''
        studenti = self.student_repository.read()
        note = self.nota_repository.read()
        k = []
        r = {}
        for s in studenti:
            if s.tip_bursa not in k:
                k.append(s.tip_bursa)
        for i in k:
            j = 0
            h = 0
            for s in studenti:
                if s.tip_bursa == i:
                    j += self.get_medie(s)
                    h += 1
            if h != 0:
                r[i] = j / h
            else:
                r[i] = j
        return r

    def get_medie(self, s: Student):
        '''
        Getter pt media aritmetica a notelor
        unui student.
        :return:
        '''
        note = self.nota_repository.read()
        k = 0
        j = 0
        for n in note:
            if n.id_student == s.id_entity:
                k += 1
                j += n.nota
        if k != 0:
            c = j/k
        else:
            c = 0;
        return c

    def export_json(self, export_filename):
        """
        Exporta  un fișier JSON  cheile sunt numele materiilor
        iar valoarea unei chei este o lista cu toti studentii
        care au avut cel putin media 5.
        :param export_filename: numele fisierului in case se exporta.
        """
        result = {nota.materie: [] for nota in self.nota_repository.read()}
        note = self.nota_repository.read()

        studenti = self.student_repository.read()
        for nota in self.nota_repository.read():
            result[nota.materie].append(self.student_repository.read(nota.id_student).nume)

        for nota in note:
            ids_from_note = [nota.id_entity for x in studenti
                             if x.id_entity == nota.id_student and
                             self.get_medie(x) >= 5]
            result[nota.materie] = [self.student_repository.read(id_entity).nume
                                    for id_entity in ids_from_note]
        with open(export_filename, 'w') as f:
            json.dump(result, f, indent=2)
