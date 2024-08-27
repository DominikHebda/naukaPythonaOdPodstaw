fo = open("text.txt", "r")
print("Nazwa pliku:", fo.name)

line = fo.readline()
print("Czytaj linię: >" + line + "<")

# Ponownie ustaw wskaźnik na początek
fo.seek(0, 0)  # f.seek(0)
line = fo.readline()
print("Czytaj linię: >" + line + "<")

fo.seek(0, 0)  # f.seek(0)

# Otwórz plik
f = open("text.txt", "r")
print("Nazwa pliku: ", f.name)

# Uzyskaj aktualną pozycję pliku.
pos = f.tell()
print("Aktualna pozycja: " + str(pos))

line = f.readline()
print("Czytaj linię: >" + line + "<")

# Uzyskaj aktualną pozycję pliku.
pos = f.tell()
print("Aktualna pozycja: " + str(pos))

# Zamknij otwarty plik
f.close()


import os
os.system('dir')


txt = open("text.txt")
print(txt.read())
txt.close()


def file_readlines(file_name):
    with open(file_name, encoding="UTF-8") as new_file:
        content_list = new_file.readlines()
        return content_list

print(file_readlines("text.txt"))



def write_readline(file_name, lista):
    file = open(file_name, "w")
    for line in lista:
        file.write(str(line + "\n"))
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


write_readline("text.txt", color)


def longest_word(filename):
    max_word = ""
    with open(filename, "r") as file:
        words = file.read().split()
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return word


print(longest_word("text.txt"))



l = 0
with open("text.txt") as f:
    for i in f:
        l += 1
print("Liczba wierszy w pliku:", l)


with open('abc.txt', 'a') as myfile:
    myfile.write("Ćwiczenia z Pythona\n")
with open('abc.txt', 'r') as myfile:
    print(myfile.read())



import os
statinfo = os.stat('text.txt')
print("Statystyka zwykłego pliku: ", statinfo)
