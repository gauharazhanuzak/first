#1
def squares(N):
    for i in range(N):
        yield i**2

N = int(input())
generator = squares(N)

for square in generator:
    print(square)

#2
def even_numbers(N):
    for i in range(0, N+1, 2):
        yield i

N = int(input())
even = even_numbers(N)
print("Even numbers between 0 and", N, ":", ', '.join(map(str, even)))

#3
def divisible_by_3_and_4_generator(N):
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

N = int(input("Enter the value of N: "))
divisible_numbers = divisible_by_3_and_4_generator(N)
print("Numbers divisible by 3 and 4 between 0 and", N, ":", ', '.join(map(str, divisible_numbers)))

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2


a, b = 2, 5
for square in squares(a, b):
    print(square)

#5
def numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1

n = 5
for num in numbers_down_to_zero(n):
    print(num)