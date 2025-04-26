#1- Single quote #
print('This is the life')
print('What\'s your name?\n')   # I have to put escape character if I'm using single quote string
print('printing bachslash \\')   # you have to escape the backslash here to print it

#2- Double quotes #
print("What's your name?\n")   # No need for escape character in a double quotes string
print("printing bachslash \\")   # you have to escape the backslash here to print it


#Escape sequence 
print("This is the first sentence.\
    This is the second sentence.")

#3- Triple quotes #
# it allow to use multiline and also to use special characters without using \
# You can print backslash without escape character
print(''' This is a multiline string. This is the first line.
      This is the second line.
      "What's your name? ", I asked.
      \ He said\n "Bond, James Bond".
      ''')

print(""" This is a multiline string. This is the first line.
      This is the second line.
      "What's your name? ", I asked.
      \ He said "Bond, James Bond".
      """)

#4-Raw Strings
# If you need to specify some strings where no special processing such as escape sequences are handled, then what you need is to specify a raw string by prefixing r or R to the string. An example is r"Newlines are indicated by \n".
print(r'New lines are \ /indicated by \n')
print(r"New lines are \ / indicated by \n")
print(r'''New lines are \ / indicated by \n''')