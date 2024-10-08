from Domain.nota import Nota


class NotaValidator:
    def validate(self, nota: Nota):
        errors = []
        if nota.materie == '':
            errors.append('Materie invalida(nu poate fi string nul).')
        if nota.id_student == '':
            errors.append('Id-ul studentului nu poate fi nul.')
        if errors:
            raise ValueError(errors)
