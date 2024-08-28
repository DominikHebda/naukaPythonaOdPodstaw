import datetime

temperatury = [
    37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
    35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
    39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
    36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
    33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
    39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
    34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
    34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
    34.2, 40.2, 34.3, 35.3
]


wynik = list(filter(lambda x: x >= 40.0, temperatury))
print(wynik)
wynik_sort = sorted(wynik)
print(wynik_sort)

ludzie = {'Jan': 40, 'Maria': 20}
print(list(filter(lambda x: ludzie[x] < 30, ludzie)))

from statistics import mean
sr_temp = mean(temperatury)
print(sr_temp)


odch = list(map(lambda x: x - sr_temp, temperatury))
print(odch)

odch = list(map(lambda x: round(x - sr_temp, 1), temperatury))
print(odch)

x = lambda a: a
print(x(3))


x = lambda z: z + 15
print(x(5))


q = lambda a, b: a * b
print(q(2, 3))


subject_marks = [('Język angielski', 88),
                 ('Nauka',           90),
                 ('Matematyka',      97),
                 ('Nauki społeczne', 82)]
print("Oryginalna lista krotek:")
print(subject_marks)

r = sorted(subject_marks, key=lambda q : q[1])

subject_marks.sort(key=lambda x : x[1])
print("\nSortowanie listy krotek:")
print(subject_marks)


models = [{'marka': 'Nokia',   'model': '3310',   'kolor': 'Czarny'},
          {'marka': 'Apple',   'model': '11',     'kolor': 'Złoty'},
          {'marka': 'Samsung', 'model': 'Galaxy', 'kolor': 'Srebrny'}]
print("Oryginalna lista słowników:")
print(models)
sorted_models = sorted(models, key=lambda x: x['model'])
print("\nSortowanie listy słowników:")
print(sorted_models)


starts_with = lambda x: x.startswith('P')
print(starts_with('Python'))
print(starts_with('Java'))


import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))


m = lambda b: b.replace('.', '', 1).isdigit()
n = lambda r: m(r[1:]) if r[0] == '-' else m(r)
print(n("334.65"))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Oryginalna lista liczb całkowitych:")
print(nums)
print("\nParzyste liczby ze wspomnianej listy:")
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
print("\nNieparzyste liczby ze wspomnianej listy:")
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)


array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
print("Oryginalne tablice:")
print(array_nums1)
print(array_nums2)
result = list(filter(lambda x: x in array_nums1, array_nums2))
print("\nPrzecięcie wspomnianych tablic:", result)



array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print("Oryginalna tablica:")
print(array_nums)
odd_ctr = len(list(filter(lambda x: x % 2 != 0, array_nums)))
even_ctr = len(list(filter(lambda x: x % 2 == 0, array_nums)))
print("\nLiczba liczb parzystych w powyższej tablicy: ", even_ctr)
print("\nLiczba liczb nieparzystych w powyższej tablicy: ", odd_ctr)