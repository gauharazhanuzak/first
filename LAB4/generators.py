#1
def squares(N):
    for i in range(N):
        yield i**2

N = int(input())
t = squares(N)

for square in t:
    print(square)

#2
def even_numbers(N):
    for i in range(0, N+1, 2):
        yield i

N = int(input())
even = even_numbers(N)
print("Even numbers between 0 and", N, ":", ', '.join(map(str, even)))

#3
def div_generator(N):
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

N = int(input())
numbers = div_generator(N)
print("Numbers divisible by 3 and 4 between 0 and", N, ":", ', '.join(map(str, numbers)))

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2


a, b = 3,4
for s in squares(a, b):
    print(s)

#5
def numbers(n):
    while n >= 0:
        yield n
        n -= 1

n = 7
for num in numbers(n):
    print(num)