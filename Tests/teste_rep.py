from Domain.student import Student
from Repository.json_repository import JsonRepository
from utils import clear_file


def test1_repository():
    '''
    Teste pentru 'student' repository
    '''
    filename = 'test1_repo.json'
    clear_file(filename)
    student_repository = JsonRepository(filename)
    added = Student('1', 'a', 2020, 'de merit')
    student_repository.create(added)
    assert student_repository.read(added.id_entity) == added


def test2_repository():
    '''
    Teste pentru 'y' repository
    '''
    filename = 'test2_repo.json'
    clear_file(filename)
#   card_repository = JsonRepository(filename)
#   added = entity
#   card_repository.create(added)
#   assert card_repository.read(added.id_entity)==added
#   updated = entity
#   card_repository.update(updated)
#   assert y_repository.read(updated.id_entity)==updated
#   added1 = entity
#   y_repository.create(added1)
#   y_repository.delete(added1.id_entity)
#   assert y_repository.read(added1.id_entity) is None


def test_repository():
    test1_repository()
    test2_repository()
