from Domain.notavalidator import NotaValidator
from Domain.studentvalidator import StudentValidator
from Repository.json_repository import JsonRepository
from Service.nota_service import NotaService
from Service.student_service import StudentService
from Tests.teste_rep import test_repository
from UserInterface.console import Console


def main():
    nota_repository = JsonRepository('nota.json')
    student_repository = JsonRepository('student.json')
    nota_validator = NotaValidator()
    student_validator = StudentValidator()
    nota_service = NotaService(nota_repository, nota_validator, student_repository)
    student_service = StudentService(student_repository, student_validator)

    console = Console(nota_service, student_service)
    console.run_console()


if __name__ == '__main__':
    test_repository()
    main()
