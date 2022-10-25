class Persoana:
    def __init__(student,medie_generala,nume_facultate):
        student.medie = medie_generala
        student.facultate = nume_facultate

class Student(Persoana):
    def __init__(student, medie_generala, nume_facultate, nume, varsta, prenume):
        super().__init__(medie_generala, nume_facultate)
        student.nume = nume
        student.varsta = varsta
        student.prenume = prenume

    def SchimbareMedie(student, medienoua):
        student.medie = medienoua

print("Introduceti niste date despre student\n")
Student.nume = input('Nume: ')
Student.prenume = input('Prenume: ')
Student.varsta = input('Varsta: ')
Student.medie = input('Medie Generala: ')
Student.facultate = input('Numele Facultatii: ')

Raspuns = input('Media sa este ' + Student.medie +'. Vrei sa schimbam media generala? 1. Da 2. Nu\n')

if Raspuns == '1':
    MedieNoua = input("Care vrei sa fie media acestuia? \n")
    Student.SchimbareMedie(Student, MedieNoua)
    print("Acum media sa este: " + Student.medie)
else:
    print("Media sa nu s-a schimbat")

k=input("Apasa pe orice pentru a inchide\n") 