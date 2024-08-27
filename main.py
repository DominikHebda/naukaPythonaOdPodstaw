while True:
    try:
        num1 = int(input('Liczba 1:'))
        num2 = int(input('Liczba 2:'))
        print(f'Suma to: {num1+num2}')
        break
    except ValueError:
        print('Wprowadź dane liczbowe')



a = 5
b = 0
try:
    result = a / b
except ZeroDivisionError:
    result = "Nie możesz podzielić przez 0"

print(result)


a = [1, 2, 5]
try:
    print(a[3])
except IndexError:
    pass


text = 'abc2'
try:
    msg = text + 5
except TypeError:
    msg = "Nie możesz dodać int do str"

print(msg)


list = [2, 3, 4]

try:
    msg = list[5]
except IndexError as error:
    msg = "Jesteś poza zakresem listy (" + str(error) + ")"
print(msg)


a = int(input('Podaj pierwszą liczbę:'))
b = int(input('Podaj drugą liczbę:'))


def division(a, b):
    try:
       divide = a / b
    except ZeroDivisionError as e:
        print(f"Wystąpił błąd:{e}")
    else:
        print(f"Wynik dzielenia to: {divide}")


print(division(a, b))

z = int(input("Podaj cenę netto:"))
v = 1.23


def multiply_Vat(z, v):
    try:
        if z <= 0:
            raise ValueError("Cena nie może być ujemna!")
        multiply = z * v
        print(f"Cena brutto: {multiply} zł")
    except ValueError as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        print("Obliczenie zakończone")

multiply_Vat(z, v)


c = int(input('Podaj pierwszą liczbę:'))
d = int(input('Podaj drugą liczbę:'))


def division(a, b):
    try:
       divide = c / d
    except ZeroDivisionError as e:
        print(f"Wystąpił błąd:{e}")
    else:
        print(f"Wynik dzielenia to: {divide}")
    finally:
        print("obliczenie zakończone")


print(division(c, d))


def process_sensor_data(value_s, type_s):
    try:
        if not isinstance(value_s, (int, float)):
            raise TypeError ("Wartość musi być liczbą")
        if type_s not in ["temperatura", "ciśnienie", "wilgotność"]:
            raise ValueError ("Nieznany typ sensora")
    except Exception as e:
        print((f"Wartość musi być liczbą: {e}"))
    else:
        print(f"Wartość sensora to: {value_s}, Typ sensora to: {type_s}")
    finally:
        print("Przetwarzanie zakończone")


process_sensor_data(25.5, "temperatura")
process_sensor_data("niepr", "ciśnienie")
process_sensor_data(1010.5, 'Niezna')



