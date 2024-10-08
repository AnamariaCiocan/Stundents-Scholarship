from Domain.student import Student


class StudentValidator:
    def validate1(self, student: Student):
        errors = []
        if student.nume == '':
            errors.append('Studentul nu poate avea numele nul.')
        if errors:
            raise ValueError(errors)
