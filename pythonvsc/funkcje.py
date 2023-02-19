'''
def moja_funkcja():
    print("Hello World!")

moja_funkcja()


def moja_funkcja2(text):
    print(text)

moja_funkcja2("Hello World!")

def moja_funkcja3(text,text2):
    print(text,text2)

moja_funkcja3("Hello World!", "Hello Poland!")

def funkcja_arg(arg1="1",arg2="2",arg3="3"):  # w cudzyslowiu argumenty domyslne
    return arg1,arg2,arg3

print(funkcja_arg(arg2="pl")) #zmiana domyslnego argumentu
'''

#Zdefiniuj funkcję, która będzie pobierała dwie wartości liczbowe i zwracała sumę tych wartości 

def suma_sposob1(liczba1,liczba2):
    return liczba1 + liczba2

def suma_sposob2(liczba1,liczba2):
    suma = liczba1 + liczba2
    return suma

print(suma_sposob1(3,5))
print(suma_sposob2(3,5))

#Zdefiniuj funkcję, która będzie pobierała dwie wartości liczbowe i zwracała sumę oraz różnicę tych wartości w jednym poleceniu return

def suma_i_roznica1(liczba1,liczba2):
    return liczba1+liczba2, liczba1 - liczba2

def suma_i_roznica2(liczba1,liczba2):
    dodawanie = liczba1+liczba2
    odejmowanie = liczba1 - liczba2
    return dodawanie, odejmowanie

 print(suma_i_roznica1(10,3)) 
 print(suma_i_roznica2(10,3))



# Zdefiniuj funkcję, która pobierze jedną wartość liczbową i wykona takie założenia:
# jeśli zostanie przekazana wartość argumentu podczas odwołania się do funkcji, to zwraca kwadrat tej liczby
# jeśli nie zostanie przekazana żadna wartość do funkcji, to zwraca liczbę 0 (zero)(zastosuj instrukcję warunkową if)

def zadanie_3(liczba="hello"):
    if liczba != "hello"
        return liczba**2
        else:
            return 0

print(zadanie_3(3))

    