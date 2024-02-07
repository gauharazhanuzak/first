#1
def function(grams):
    ounces = 28.3495231 * grams
    return ounces


#2
def function(F):
    C=(5 / 9) * (F - 32)
    return C


#3
numheads=35
numlegs=94
def solve(numheads,numlegs):
    for num_chickens in range(numheads+1):
        num_rabbits=numheads-num_chickens
        total=2*num_chickens+4*num_rabbits
        if total==numlegs:
            return  num_chickens,num_rabbits
print(solve(numheads,numlegs))


#4
numbers = [2, 3, 8, 11, 15, 17, 20]
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
print(filter_prime(numbers))

#5
from itertools import permutations

def print_permutations():
    s = input()
    t = permutations(s)
    for i in t:
        print(''.join(i))
print_permutations()

#6
def reversed(s):
    words = s.split()
    i = len(words) - 1
    while i >= 0:
        print(words[i], end=' ')
        i -= 1

s = input()
reversed(s)


#7
def has_33(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == 3:
            if nums[i+1] == 3:
                return True
        i += 1
    return False

numbers = input()
nums = numbers.split()
nums = [int(num) for num in nums]
print(has_33(nums))


#8
def spy_game(nums):
    s = ''
    for i in nums:
        s += i
    if '007' in s:
        return True
    return False

numbers = input()
nums = numbers.split()
print(spy_game(nums))


#9
def radius(r):
    sphere = 4/3*3.14*r**3
    return sphere 

r = int(input())
print(radius(r))


#10
def unique(l):
    list1 = []
    i = 0
    while i < len(l):
        t = True
        j = 0
        while j < i:
            if l[i] == l[j]:
                t = False
            j += 1
        if t:
            list1.append(l[i])
        i += 1
    return list1

l = input()
elements = l.split()
list1 = unique(elements)
print(list1)


#11
def palindrome(s):
    i = 0
    j = len(s)-1
    while i < len(s)/2:
        if s[i] != s[j]:
            return 'No'
        i+=1
        j-=1
    return 'palindrome'

s = input()
print(palindrome(s))


#12 
def histogram(t):
    i = 0
    while i < len(t):
        j = 0
        while j < t[i]:
            print('*', end='')
            j += 1
        print()
        i += 1

t = input()
t = t.split()
t = [int(num) for num in t]
histogram(t)


#13
import random

def find(num, t):
    t += 1
    num2 = int(input('Take a guess.\n'))
    if num2 == num:
        print(f'Good job, KBTU! You guessed my number in {t} guesses!')
        return
    print('\nYour guess is too low.')
    return find(num, t)

name = input('Hello! What is your name?\n')
num = random.randint(1, 20)
t = 0
print(f'Well, {name}, I am thinking of a number between 1 and 20.\n')
find(num, t)
