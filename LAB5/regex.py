#1
import re

example = "abc dhhud djk"
r=re.compile(r'ab*')

print (re.search(r, example))

#2
import re

example = "fr jrabbbfn abb"
r=re.compile(r'ab{2,3}')

print(re.findall(r, example))

#3
import re

r = re.compile(r'[a-z]+_[a-z]+')
example = 'word_example'
print(re.findall(r, example))

#4
import re

r = re.compile(r'[A-Z][a-z]+')
example = 'HelloWorld ExampleText'
print(r.findall(example))

#5
import re

r = re.compile(r'a.*b$')
example = 'a random text b'
print(r.findall(example))

#6
import re

r = re.compile(r'[ ,.]+')
example = 'This is, a sample. String'
result = r.sub(':', example)
print(result)

#7
def snake_to_camel(snake_case):
    words = snake_case.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

example = 'snake_case_example'

print(snake_to_camel(example))

#8
import re

r = re.compile(r'[A-Z][a-z]*')
example = 'SplitAtUppercaseLetters'

print(r.findall(example))

#9
import re

r = re.compile(r'([a-z])([A-Z])')
example= 'InsertSpacesBetweenWords'
print(r.sub(r'\1 \2', example))

#10
import re

def camel_to_snake(c):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', c).lower()

example = 'camelCaseExample'
print(camel_to_snake(example))