import jsonpickle
from typing import Dict, Union, Optional, List, Type

from Domain.entity import Entity
from Repository.repository import Repository


class JsonRepository(Repository):

    def __init__(self, filename):
        self.filename = filename

    def __read_file(self):
        '''
        Citeste fisierul
        :return:fisierul sau {} daca
                apare o exceptie
        '''
        try:
            with open(self.filename, 'r') as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __write_file(self, objects: Dict[str, Entity]):
        with open(self.filename, 'w') as f:
            f.write(jsonpickle.dumps(objects))

    def create(self, entity: Entity) -> None:
        '''
        Creeaza o entitate
        :param entity: noua entitate
        '''
        entities = self.__read_file()
        if self.read(entity.id_entity) is not None:
            raise KeyError(f'Exista deja o '
                           f'entitate cu id-ul {entity.id_entity}.')

        entities[entity.id_entity] = entity
        self.__write_file(entities)

    def read(self, id_entity: object = None) \
            -> Type[Union[Optional[Entity], List[Entity]]]:
        '''
        Citeste o entitate din 'baza de date'
        :param id_entity: id-ul entitatii care
                        este 'citita'
        :return: entitatea daca id-ul exista;
                None daca nu exista o
                entitate cu id-ul dat;
                lista de entitati daca
                 id_entity=None
        '''
        entities = self.__read_file()
        if id_entity:
            if id_entity in entities:
                return entities[id_entity]
            else:
                return None

        return list(entities.values())

    def update(self, entity: Entity) -> None:
        '''
        Actualizeaza o entitate existenta
        :param entity: entitatea ce trebuie
                        actualizata
        '''
        entities = self.__read_file()
        if self.read(entity.id_entity) is None:
            msg = f'Nu exista o entitate cu id-ul ' \
                  f'{entity.id_entity} de actualizat.'
            raise KeyError(msg)

        entities[entity.id_entity] = entity
        self.__write_file(entities)

    def delete(self, id_entity: str) -> None:
        '''
        Sterge o entitate dupa id-ul dat.
        :param id_entity: id-ul entitatii
                        care trebuie stearsa
        '''
        entities = self.__read_file()
        if self.read(id_entity) is None:
            raise KeyError(
                f'Nu exista o entitate cu id-ul '
                f'{id_entity} pe care sa o stergem.')

        del entities[id_entity]
        self.__write_file(entities)
