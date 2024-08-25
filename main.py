def str_lenght(str1):
    count = 0
    for char in str1:
        count += 1
    return count

print((str_lenght('Python')))


Lista = [1, 2, -8]
lst = [2, 3, 5]


def sum_el_list(lst):
    sum_list = 0
    for el in lst:
        sum_list += el
    return sum_list


print(sum_el_list(Lista))
print(sum_el_list(lst))


def multiple_list(arg):
    multi_list = 1
    for el in arg:
        multi_list *= el
    return multi_list


print(multiple_list(Lista))
print(multiple_list(lst))


list = [1, 2, -8, 0]


def max_number(numbers):
    max= numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max


print(max_number(list))


def fib(n):

    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


for i in range(8):
    print(fib(i))


