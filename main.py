#Następne ćwiczenia

def add(x, y):
    print('x =', x, ', y =', y)
    return x + y


print(add(2, 3))
# print(add(x=2, y=3))
# print(add(2,))

def my_function():
    """Dokumentacja funkcji"""
help(my_function)


def fibbonaci_numbers(n):
    '''Zwraca liczby Fibonacciego mniejsze od n'''
    wynik = []
    a, b = 0, 1
    while a < n:
#     while len(wynik) <= n:
        wynik.append(a)
        a, b = b, a + b
    return wynik

x = fibbonaci_numbers(300)
print(x)

def string_lenght(str1):
    count = 0
    for char in str1:
        count += 1
    return count

print(string_lenght('Dominik'))

list1 = [8, -2, -5, 45, 77, 3]
def list_lenght(list1):
    count = 0
    for el in list1:
        count += el
    return count

print(list_lenght(list1))

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


print(sum_list([1, 2, -8]))

def multiply_list(items):
    tot = items[0]
    for x in items[1:]:
        tot *= x
    return tot

print(multiply_list([2,3,4]))


def biggest_number(lista):
    maks = lista[0]
    for a in lista:
        if a > maks:
            maks = a
    return maks

print(biggest_number((1, 3, 6, 33, 4, 7, 1245, 13, 5)))


def char_frequency(str1):
    dictionary = {}
    for n in str1:
        my_keys = dictionary.keys()
        if n in my_keys:
            dictionary[n] += 1
        else:
            dictionary[n] = 1
    return dictionary

print(char_frequency('google.com'))


def match_words(words):
    list = 0
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]:
            list += 1
    return list

print(match_words(['a', 'abc', 'xyz', 'aba', '1221']))


def last(n):
    return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


