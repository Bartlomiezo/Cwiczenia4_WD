import random
import math
#ZAD 1
a=[1-x for x in range(1,11)]
print(a)
b=[4**y for y in range(0,8)]
print(b)
c=[v for v in a if v%2==0]
print(c)
#ZAD 2
lista1=[]
for i in range(0,10):
    lista1.append(random.randint(0,100))
print(lista1)
lista2=[x for x in lista1 if x%2==0]
print(lista2)
#ZAD 3
zakupy1={"JAJKA":"SZTUKI","CUKIER":"KILOGRAMY", "MLEKO":"LITRY"}
zakupyodwrocone={value:key for key, value in zakupy1.items()}
print(zakupyodwrocone)
#ZAD 4
def czy_prostokatny(a,b,c):
    if(a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==c**2):
        print("Jest prostokątny")
        return 0
    else:
        print("Nie jest prostokątny")
        return 0
czy_prostokatny(3,4,6)
#ZAD 5
def pole_trapezu(a=0,b=0,h=0):
    print(((a+b)*h)/2)
    return 0
pole_trapezu(1,2,3)
pole_trapezu(1,2)
#ZAD 6
def iloczyn_elementow(a=1,b=4,ile=10):
    iloczyn=1
    nastepna_liczba=a
    for i in range(0,ile):
        iloczyn*=nastepna_liczba
        nastepna_liczba*=b
    print(iloczyn)
iloczyn_elementow()
#ZAD 7
def iloczyn_elementow2(* liczby):
    iloczyn=1
    for i in liczby:
        iloczyn*=i
    print(iloczyn)
iloczyn_elementow2(1,2,3,4)
#ZAD 8
def zakupy(** przedmioty):
    print("Ilosc przedmiotow równa sie "+ str(len(przedmioty)))
    suma=0
    for i in przedmioty.values():
        suma+=i
    print("Wartość zakupów to "+ str(suma))
zakupy(cebula= 3, mleko=4)
#ZAD 9
liczbadopierwiastka=input("PODAJ LICZBE: ")
liczbadopierwiastka=int(liczbadopierwiastka)
try:
    liczbadopierwiastka=math.sqrt(liczbadopierwiastka)
    print("Pierwiastek z tej liczby wynosi "+ str(liczbadopierwiastka))
except ValueError:
    print("Podana liczba jest ujemna")