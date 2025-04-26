# convert characters to lower  charaacters
phrase = "Hello Ahmed AlI"
print(phrase.lower())

# convert characters to upper case  charaacters
print(phrase.upper())

# Check characters if they are upper case characters
print(phrase.upper().isupper())

# Check characters if they are lower case charaacters
print(phrase.upper().islower())

# Get the len Length of string characters
print(len(phrase))
print("********** 1 ****")
# Get certain character using the index
print(phrase[0])  # access the first character
print(phrase[1])
print(phrase[2])
print("********** 2 ****")

# Get the index of first character A in the string
print(phrase.index('A'))
print(phrase.index('H'))
print(phrase.index('l'))
# get the index for the part med string in the array
print(phrase.index('med'))
# if u searched index for non existing characters, it will give error
# print(phrase.index('z'))

# replace a word in sring with one another string
name = "Giraff Academy"
print(name.replace('Giraff', "Elephant"))
