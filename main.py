# Przykładowy komentarz - abc
print('Hello world!')

# Biorąc pod uwagę string o dowolnej liczbie znaków, zwróć substring złożony z trzech środkowych znaków danego stringu:
# Przypadek 1:
# sample_str = "Datatypes"
# Oczekiwany wynik: aty
# Przypadek 2:
# sample_str = "FullStack"
# Oczekiwany wynik: lSt
# Przypadek 3:
# sample_str = "Python"
# Oczekiwany wynik: yth albo tho

sample_str = "Datatypes"
middle_index = int(len(sample_str) / 2)
print("Oryginalny ciąg to:", sample_str)
middle_three = sample_str[middle_index - 1:middle_index + 2]
print("To są trzy środkowe znaki:", middle_three)

sample_str = "FullStack"
middle_index = int(len(sample_str) / 2)
print("Oryginalny ciąg to:", sample_str)
middle_three = sample_str[middle_index - 1:middle_index + 2]
print("To są trzy środkowe znaki:", middle_three)

sample_str = "Python"
middle_index = int(len(sample_str) / 2)
print("Oryginalny ciąg to:", sample_str)
middle_three = sample_str[middle_index - 1:middle_index + 2]
print("To są trzy środkowe znaki:", middle_three)




# Biorąc pod uwagę 2 ciągi, s1 i s2, utwórz nowy ciąg, dodając s2 w środku s1
# Dane:
# s1 = "FullStack"
# s2 = "Python"
# Oczekiwany wynik:
# FullPythonStack

s1 = "FullStack"
s2 = "Python"
middle_index = len(s1) // 2
print(middle_index)
s3 = s1[:middle_index]
s4 = s1[middle_index:]
print(s3)
print(s4)
s5 = s3 + s2 + s4
print(s5)

#Biorąc pod uwagę 2 ciągi, s1 i s2 zwróć nowy ciąg złożony z pierwszego, środkowego i ostatniego znaku każdego ciągu wejściowego
# Dane:
# s1 = "America"
# s2 = "Japan"
# Oczekiwany wynik:
# AJrpan

s1 = "America"
s2 = "Japan"
first_char = s1[0] + s2[0]
middle_char = s1[len(s1) // 2] + s2[len(s2) // 2]
last_char = s1[-1] + s2[-1]
res = first_char + middle_char + last_char
print("Mix String to:", res)

#Odwróć podany ciąg: Python

sample_str = "Python"
print("Oryginalny ciąg to:", sample_str)
sample_str = sample_str[::-1]
print("Odwrócony ciąg to:", sample_str)

#Ćwiczenie — odwróć krotkę

tuple1 = (10, 20, 30, 40, 50)
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)

#Ćwiczenie — dostęp do wartości 20 z krotki

sample_tuple = ("Pomarańczowy", [10, 20, 30], (5, 15, 25))
print(sample_tuple[0])
print(sample_tuple[1])

print(sample_tuple[1][1])

#Zadanie
#Utwórz listę zawierającą imiona wszystkich kursantów
#Następnie ją posortuj alfabetycznie, oraz
#Sprawdź ile elementów ona zawiera

list = ["Piotr", "Marzena", "Marcin", "Grzegorz", "Katarzyna", "Michał"]
print(sorted(list))
x = len(list)
print(x)

#Ćwiczenie — zamień dwie listy na słownik
#Poniżej znajdują się dwie listy. Napisz program w Pythonie konwertujący je na słownik w taki sposób, że pozycja z listy 1 jest kluczem, a pozycja z listy 2 jest wartością

keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
values = [10, 20, 30]
res_dict = dict(zip(keys, values))
print(res_dict)

#Ćwiczenie — dodaj listę elementów do zbioru
#Mając listę Pythona, napisz program, który doda wszystkie jej elementy do danego zbioru.

sample_set = {"Żółty", "Pomarańczowy", "Czarny"}
sample_list = ["Niebieski", "Zielony", "Czerwony"]
sample_set.update(sample_list)
print(sample_set)

# Next excercise

nl = []
for x in range(1500, 2701):
    if x % 7 == 0 and x % 5 == 0:
        nl.append(str(x))
print(nl)


#ndx = []
#x = input("Podaj pierwszą liczbe:")
#for x in range(2, x <= x):
#    if x % 2 == 0:
#        ndx.append(int(x))
#print(ndx)


#ndy = []
#y = input("Podaj pierwszą liczbe:")
#for y in range(2, y <= y):
#    if y % 2 == 0:
#        ndy.append(int(y))
#print(ndy)


row = 5
for i in range(1, row +1):
    for j in range(1, i +1):
        print(j, end='')

    print()


s = 0
n = int(input("Podaj liczbę:"))
for n in range(0, n + 1):
    s += i
print("\n")
print("Suma to:", s)

n = int(input("Podaj liczbę:"))
x = sum(range(0, n + 1))
print("\n")
print("Suma to:", s)

