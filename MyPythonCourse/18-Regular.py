import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
1234567890

Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? {  [ ] \ ( )
123.355.2331
321-555-4321
coreyms.com
Mr. Schafer
Ms Davis
Mr.T
'''
# Get the pattern of raw string literally that has exact string 'abc'
pattern = re.compile(r'abc')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

print('============(example 1) print all matches for "abcd" in a string')

# print all matches
for match in matches:
    print(match)

# check the string slices from 1 to 4
print(text_to_search[1:4])
# It will print all matches, span gives the number of the character as the begining of that match and the endingings character nubmer of the match.
# <re.Match object; span=(1, 4), match='abc'>  --> it finds a match at character number 1 and end at character number 4
# <re.Match object; span=(55, 58), match='abc'>  --> again another match at character number 28 till character 31

# ---------------------- Reqular expressions ----------- #
# .     matches any character except a new line
# \d    matches any digit (0-9)
# \D    matches any character which is not a digit
# \w    mathces any word character (a-z, A-Z, 0-9, _)
# \W    matches any character that is not a word character
# \s    matches any character that is a white space ( space, tab, newline )
# \S    mathces any character that is not a white space ( not space, not a tab, not a newline)
# \b    mathces a word boundry for some word start by a sequence of characters or have a space before that sequence
# \B    mathces any character that is not a word boundary
# --------------------------------- #
print('============(example 2) print all matches for "." in a string')
# Get the pattern of raw string literally that has exact string 'abc'
pattern = re.compile(r'.')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# . is a special character in regualr expressions means for any character that is existed every where in the string,
# So we need to escape it with backslash
# --------------------------------- #
print('============(example 3) print all matches for "." in a string')
pattern = re.compile(r'\.')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# --------------------------------- #
print('============(example 4)  search coreyms.com in the string')
pattern = re.compile(r'coreyms\.com')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print('============(example 5)  search any digit between 0 and 9 the string')
pattern = re.compile(r'\d')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print('============(example 6)  search any character except digits between 0 and 9 the string')
pattern = re.compile(r'\D')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print('============(example 7)  search any word character (a-z, A-Z, 0-9, _)')
pattern = re.compile(r'\w')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print('============(example 8)  search anything that is not a word character (a-z, A-Z, 0-9, _)')
pattern = re.compile(r'\W')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print('============(example 9)  search any thing that is a white space ( space, tab, newline )')
pattern = re.compile(r'\s')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print('============(example 10)  search any thing that is not a white space ( space, tab, newline )')

pattern = re.compile(r'\S')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print('============(example 11)  search any that has word boundary start by Ha )')
# it will match any word boundary that start by (Ha) or (space then Ha)
pattern = re.compile(r'\bHa')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


print('============(example 12)  search for any starting word \'This\' of a string  )')

sentence = 'This is a sequence and then it brings it to an end'
pattern = re.compile(r'^has')  # has is not a start of a string, so no match
# find that pattern in the text to search
matches = pattern.finditer(sentence)

for match in matches:
    print(match)

# This is a start word of the string and will give match
pattern = re.compile(r'^This')
# find that pattern in the text to search
matches = pattern.finditer(sentence)

for match in matches:
    print(match)


print('============(example 13)  search for any ending word \'an\' of a string  )')

pattern = re.compile(r'an$')  # has is not a start of a string, so no match
# find that pattern in the text to search
matches = pattern.finditer(sentence)

for match in matches:
    print(match)


print('============(example 14)  search for any ending word \'end\' of a string  )')

# This is a start word of the string and will give match
pattern = re.compile(r'end$')
# find that pattern in the text to search
matches = pattern.finditer(sentence)

for match in matches:
    print(match)

print('============(example 15)  search for any digits in such format 123.355.2331 / 123.455.2331 / 321-555-4321 )')
#  find any 3 digits then any character '.' then any 3 digits then any character '.' then any 4 digits
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# find that pattern in the text to search
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
