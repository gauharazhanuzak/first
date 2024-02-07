#1
class InputAndOutput:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input()

    def printString(self):
        print(self.input_string.upper())


string = InputAndOutput()
string.getString()
string.printString()


#2
class Shape:
    def __init__(self, l=0):
        self.length = l
        
    def area(self):
        return self.length

class Square(Shape):
    def __init__(self, l=0):
        super().__init__(l)

    def area(self):
        return self.length * self.length

shape = Shape(3)
print(shape.area())

square = Square(3)
print( square.area())



#3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length
    
r = Rectangle(2, 7)
print( r.area())


#4
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'x={self.x}  y={self.y}')

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
    

p1 = Point(1, 4)
p2 = Point(6, 9)

p1.show()
p2.show()

p1.move(2, 5)
p1.show()

print(f'dist: {p1.dist(p2)}')


#5
class Bank:
    def __init__(self, money):
        self.b = money

    def balance(self):
        print(f'balance: {self.b}')

    def deposit(self, deposit):
        self.b += deposit
        print(f'deposit of {deposit} successfully made. New balance: {self.b}')

    def withdraw(self, withdraw):
        if self.b < withdraw:
            print('insufficient funds!')
        
        else:
            self.b -= withdraw
            print(f'withdrawal of {withdraw} successfully made. New balance: {self.b}')


user = Bank(2500)

user.balance()
user.deposit(200)
user.balance()
user.withdraw(2200)
user.withdraw(1000)

        
#6
class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n < 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_filter = PrimeFilter(numbers)
prime_numbers = prime_filter.filter_primes()

print("Prime numbers:", prime_numbers)