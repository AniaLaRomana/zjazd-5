### Zdefiniuj pętle wyrzucającą na konsolę liczby od 1 do 10 włącznie (za pomocą pętli for )

for i in range(1,11):
    print(i)

a = 1
while a <= 10:
    print(a)
    a += 1



### Ciąg Fibonacci - wyświetl za pomocą pętli kolejne numery ciągu Fibo od 0 do 10 elementu
### Ciąg Fibonacciego – ciąg liczb naturalnych określony rekurencyjnie w sposób następujący: Pierwszy wyraz jest równy 0, drugi jest równy 1, każdy następny jest sumą dwóch poprzednich.

liczba1 = 0
liczba2 = 1

print(liczba1)
print(liczba2)

iteracja = 0

while 0 < 10:
    kolejna_liczba = liczba1 + liczba2
    liczba1 = liczba2
    liczba2 = kolejna liczba2

    print(kolejna_liczba)

    iteracja += 1