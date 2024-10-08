from Service.nota_service import NotaService
from Service.student_service import StudentService


class Console:
    def __init__(self,
                 nota_service: NotaService,
                 student_service: StudentService):
        self.nota_service = nota_service
        self.student_service = student_service

    def show_menu(self):
        print('1. Adaugare student.')
        print('2. Adaugare nota.')
        print('3. Afisarea tuturor studentilor cu un tip'
              ' de bursa de la tastatura descrescator'
              ' dupa an.')
        print('4. Pentru fiecare tip de bursa sa se afiseze'
              ' media aritmetica a studentilor din'
              ' acea categorie.')
        print('5. Export JSON')
        print('sb. Afisare studenti.')
        print('ss. Afisare note.')
        print('x. Exit.')

    def handle_show_all(self, entities):
        for entity in entities:
            print(entity)

    def run_console(self):
        while True:
            self.show_menu()
            opt = input('Optiunea: ')
            if opt == '1':
                self.handle_add_student()
            elif opt == '2':
                self.handle_add_nota()
            elif opt == 'sb':
                self.handle_show_all(self.student_service.get_all())
            elif opt == 'ss':
                self.handle_show_all(self.nota_service.get_all())
            elif opt == '3':
                self.handle_ord_desc()
            elif opt == '4':
                self.handle_afisare_medie()
            elif opt == '5':
                self.handle_export()
            elif opt == 'x':
                break
            else:
                print('Optiune invalida.')

    def handle_add_student(self):
        try:
            id_student = input('Id-ul studentului: ')
            nume = input('Numele studentului: ')
            anul = int(input('Dati anul: '))
            tip_bursa = input('Dati tipul de bursa: ')
            self.student_service.add_student(id_student, nume,
                                             anul, tip_bursa)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_add_nota(self):
        try:
            id_nota = input('Id-ul notei: ')
            nume_materie = input('Numele materiei: ')
            nota = float(input('Nota: '))
            penalizare = int(input('Penalizare: '))
            id_student = input('Dati id-ul studentului: ')
            self.nota_service.add_nota(id_nota, nume_materie,
                                       nota, penalizare, id_student)
        except ValueError as ve:
            print('Eroare validare:', ve)
        except KeyError as ke:
            print('Eroare ID:', ke)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_export(self):
        try:
            filename = input('Numele fisierului pentru export: ')
            self.nota_service.export_json(filename)
        except Exception as ex:
            print('Eroare:', ex)

    def handle_ord_desc(self):
        '''
        Ordonarea conform cerintei 3.
        :return:lista ordonata coresupunzator.
        '''
        x = input('Dati tipul de bursa pentru'
                  ' care se vor afisa studentii: ')
        print(self.student_service.ordonare_an(x))

    def handle_afisare_medie(self):
        '''
        Afisarea studentilor dupa cerinta 4.
        :return:
        '''
        print(self.nota_service.medie_aritmetica())
