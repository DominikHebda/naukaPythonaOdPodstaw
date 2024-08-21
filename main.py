n = 2
for i in range(1, 11):
    p = n * i
    print(p)


numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i >= 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print (i)

counter = 0
number = int(input("podaj liczbę:"))
while number != 0:
    number = number // 10
    counter += 1
print("Całkowita liczba cyfr to:", counter)



row = 5
col = 5
for i in range(0, row+1):
    for j in range(col-i, 0, -1):
        print(j, end=' ')
    print()