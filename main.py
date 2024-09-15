"""Dokumentacja modułu"""

class MyClass:
    """Dokumentacja klasy"""

    def my_method(self):
        """Dokumentacja metody"""

def my_function():
    """Dokumentacja funkcji"""

help(MyClass)
help(MyClass.my_method)


class NazwaKlasy:
    atrybut_pierwszy = "Wartość"
    atrybut_drugi = 123.0




class NazwaKlasy:
    def __init__(self, trzeci):
        self.atrybut_pierwszy = "Wartość"
        self.atrybut_drugi = 123.0
        self.atrybut_trzeci = trzeci



instancja = NazwaKlasy("trzeci")

print(instancja.atrybut_pierwszy)
print(instancja.atrybut_drugi)
print(instancja.atrybut_trzeci)



class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)



class Parrot:

    # atrybut klasy
    species = "papuga"

    # atrybut instancji
    def __init__(self, name, age):
        self.name = name
        self.age = age



blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu to", blu.species)
print("Woo to również", woo.species)
print("Wszystkie obiekty klasy Papuga to", Parrot.species)

print(blu.name, "ma", blu.age, "lat")
print(woo.name, "ma", woo.age, "lat")


class Parrot:

    # atrybuty instancji
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # metoda instancji
    def sing(self, song):
        return self.name + " śpiewa " + song

    def dance(self):
        return self.name + " teraz tańczy"


blu = Parrot("Blu", 10)

print(blu.sing("'Happy'"))
print(blu.dance())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jan", 36)
print(p1.name)
print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Cześć, mam na imię " + self.name)


p1 = Person("Jan", 36)
p1.myfunc()


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Cześć, mam na imię " + abc.name)

p1 = Person("Jan", 36)
p1.myfunc()

p1.age = 40
print(p1.age)

del p1.age
#print(p1.age)


del p1
#p1.myfunc()



class KontoBankowe:
    def __init__(self, nazwa, stan = 0):
        self.nazwa = nazwa
        self.stan = stan

    def info(self):
        print("nazwa:", self.nazwa)
        print("stan:", self.stan)

    def wyplac(self, ilosc):
        self.stan -= ilosc

    def wplac(self, ilosc):
        self.stan += ilosc


jk = KontoBankowe("Jan Kowalski", 1000)
jk.info()
jk.wplac(2000)
jk.wyplac(2500)
jk.info()
jk.stan = 0  # Dostęp do składowej `stan`
jk.info()


class Jets:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

first_item = Jets("Boeing 747", "US")

print("nazwa:", first_item.name)

a=first_item.name
print(a)


class Jets:

    def __init__(self, name, origin):
        self.name = name
        self.origin = origin


first_item = Jets("Boeing 747", "US")

a = first_item.name
b = first_item.origin

print(a, b)


class Veheicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

first_car = Veheicle(240, 18000)

print(first_car.max_speed, first_car.mileage)



class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


car1 = Car("Blue", 20000)
car2 = Car("Red", 30000)

print(f"{car1.color} samochód ma  {car1.mileage}  kilometrów przebiegu.")

for car in (car1, car2):
    print(f"{car.color} samochód ma  {car.mileage:,}  kilometrów przebiegu.")



class Jets:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def print_jet(self, other_jet):
        print(self.name, self.origin)
        print(other_jet.name, other_jet.origin)


first_item = Jets("Boeing 747", "US")
second_item = Jets("Airbus A380", "EU")
third_item = Jets("Embraer 195", "BR")

fleet=[first_item.name, second_item.name, third_item.name]

print(fleet)

second_item.print_jet (third_item)



class Jets:
    def __init__(self, name, origin, quantity):
        self.name = name
        self.origin = origin
        self.quantity = quantity

first_item = Jets("Boeing 747", "US", 87)
second_item = Jets("Aiirbus A380", "EU", 35)

total = (first_item.quantity + second_item.quantity)
print(total)

jets = [Jets("Boeing 747", "US", 87), Jets("Airbus A380", "EU", 35), Jets("Embraer 195", "BR", 10)]
total = 0
for item in jets:
    total += item.quantity
print("Suma samolotów:", total)



numbers = [1, 2]
total = 0
for item in numbers:
    total += item.real
print("Suma części rzeczywistych:", total)



class Nobel:

    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner


np2005=Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005.category, np2005.year, np2005.winner)


class PySolution:

    def reverse_words(self, s):
        return ''.join(reversed(s.split()))

print(PySolution().reverse_words("hello .py"))



# class IOString:
#     def __init__(self):
#         self.str1 = "abc"
#
#     def get_string(self):
#         self.str1 = input()
#
#     def print_string(self):
#         print(self.str1.upper())
#
#
# str1 = IOString()
# str1.get_string()
# str1.print_string()


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


newRectangle = Rectangle(12, 10)

print(newRectangle.area())




import math

class Circle():

    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return 2 * self.radius * math.pi

c = Circle(8)

print(c.area())

print(c.perimeter())



class Temperature():

    def  convert_fahrenhiet(self,celsius):
        return (celsius * (9 / 5)) + 32

    def convert_celsius(self,farenhiet):
        return (farenhiet - 32) * (5 / 9)


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.age = "undefined"
        self.marks = "undefined"
    def display(self):
        print(self.name)
        print(self.roll)
        print(self.age)
        print(self.marks)
    def set_age(self, age):
        self.age = age
    def set_marks(self, marks):
        self.marks = marks



class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def add_time(self, t1, t2):
        totalHours = t1.hour + t2.hour
        totalMinutes = t1.minute + t2.minute
        totalHours += (totalMinutes // 60)
        minute = totalMinutes - ((totalMinutes // 60) * 60)
        return Time(totalHours, minute)
    def display_time(self):
        print("Czas to", self.hour, "godz. i", self.minute, "min.")

    def display_minute(self):
        print((str(self.hour * 60)) + str(self.minute))

a = Time(2, 50)
b = Time(1, 20)
b.display_minute()
c = a.add_time(a, b)
c.display_time()
c.display_minute()



import math
class Figura:

    def obwod(self):  # L/O
        """Obliczanie obwodu."""
        print("Obwód: ")

    def pole(self):  # S/P
        """Obliczanie pola powierzchni."""
        print("Pole: ")


class Koło(Figura):

    def __init__(self, r):
        self.r = r

    def obwod(self):
        super().obwod()
        return 2 * math.pi * self.r

    def pole(self):
        super().pole()
        return math.pi * self.r ** 2

f1 = Koło(5)
print(f1.obwod())
print(f1.pole())


class Trójkąt(Figura):

    def __init__(self, bok):
        self.bok = bok

    def obwod(self):
        super().obwod()
        return self.bok * 3

    def pole(self):
        super().pole()
        return ((self.bok ** 2) * 3 ** 0.5) / 4

t1 = Trójkąt(3)
print(t1.obwod())
print(t1.pole())


class TrapezProstokątny(Figura):

    def __init__(self, a, b, h):
        self.a, self.b, self.h, self.d = a, b, h, h

        e = b - a
        self.c = (h ** 2 + e ** 2) ** 0.5

    def obwod(self):
        super().obwod()
        return self.a + self.b + self.c + self.d

    def pole(self):
        super().pole()
        return ((self.a + self.b) / 2) * self.h

f3 = TrapezProstokątny(2, 4, 3)
print(f3.obwod())
print(f3.pole())


class Równoległobok(Figura):

    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def obwod(self):
        super().obwod()
        return (self.a * 2) + (self.b * 2)

    def pole(self):
        super().pole()
        return self.a * self.h


f4 = Równoległobok(2, 4, 3)
print(f4.pole())


class Równoległobok(TrapezProstokątny):
    def __init__(self, a, b, h):
        self.a, self.b, self.c, self.d, self.h = a, a, b, b, h
        # trik, dzięki któremu możemy dziedziczyć wprost
        # z trapezu prostokątnego i nie musimy wypełniać metod `obwod` i `pole`


f4 = Równoległobok(2, 4, 3)
print(f4.pole())


class Prostokąt(Figura):

    def __init__(self, a, b):
        self.a, self.b = a, b


    def obwod(self):
        super(Prostokąt, self).obwod()
        return (self.a + self.b) * 2

    def pole(self):
        super(Prostokąt, self).pole()
        return self.a * self.b


f5 = Prostokąt(2, 5)
print(f5.obwod())
print(f5.pole())


class Prostokąt(Równoległobok):
    def __init__(self, a, b):
        super().__init__(a, b, b)


f5 = Prostokąt(2, 5)
print(f5.obwod())
print(f5.pole())


class Kwadrat(Prostokąt):
    def __init__(self, a):
        super().__init__(a, a)



f6 = Kwadrat(5)
print(f6.obwod())
print(f6.pole())


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

school_bus = Bus("Szkolne Volvo", 180, 12_000)

print(
    "Nazwa pojazdu:", school_bus.name,
    "Prędkość:", school_bus.max_speed,
    "Przebieg:", f"{school_bus.mileage:,}"
)


class Vehicle:
    color = "Biały"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass



class Car(Vehicle):
    pass


school_bus = Bus("Szkolne Volvo", 180, 12_000)
print(school_bus.color, school_bus.name, "Prędkość:", school_bus.max_speed, "Przebieg:", school_bus.mileage)

car = Car("Audi Q5", 240, 18_000)
print(car.color, car.name, "Prędkość:", car.max_speed, "Przebieg:", car.mileage)



class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

school_bus = Bus("Szkolne Volvo", 12, 50_000)
print(type(school_bus))


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Liczba miejsc siedzących w {self.name} to {capacity} pasażerów"

school_vehicle = Vehicle("Szkolne Volvo", 180, 12_000)
print(school_vehicle.seating_capacity(100))



class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)

school_bus = Bus("Szkolne Volvo", 180, 12_000)
print(school_bus.seating_capacity())



class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return round(amount)


school_bus = Bus("Szkolne Volvo", 12, 50)
print("Całkowita opłata za przejazd autobusem wynosi:", school_bus.fare())


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def area(self):
        return self.length * self.width

    def display(self):
        print("Długość prostokąta to: ", self.length)
        print("Szerokość prostokąta to: ", self.width)
        print("Obwód prostokąta to: ", self.perimeter())
        print("Pole prostokąta to: ", self.area())


class Parallelepipede(Rectangle):

    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

myRectangle = Rectangle(7, 5)
myRectangle.display()
print("----------------------------------")
myParallelepipede = Parallelepipede(7, 5, 2)
print("Objętość Równoległościanu wynosi: ", myParallelepipede.volume())