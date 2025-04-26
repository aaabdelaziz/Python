
# lists in python

# Lists is like moving cursor of mouse at some place

# Courses = [ courses[0], courses[1], courses[2] ]
courses = ['History', 'Physics', 'ComputerScience', 'Math']

# length of the list
print(len(courses))

# access the value in the first item in the list
print(courses[0])

# access the value in the last item in the list, without knowing the list len
print(courses[-1])

# Error access to un existing value in the list, will give IndexError: list index out of range
# print(courses[4])

#------------------------------- Slicing ------------------------#
# show all list items starting from (0) all the way up to item(2) but not including the item (2).
print(courses[0:2])

# show all list items starting from (0) all the way up to item(1) but not including the item (1).
print(courses[0:1])

# show all list items starting from (1) all the way up to item(1) but not including the item (1).
print(courses[1:1])

# show from the beginning till the 2nd item
print(courses[:2])

# show from the second item till the end of the list
print(courses[2:])

#----------------------- List tools --------------------------------#
print('----------------------------------\n')
print(courses)

# ---------->> Add an item to the list
courses.append('Art')
print('1---------------append-------------------\n' + str(courses))

# ---------->> Extend the original old list with new items insted of inserting a new list into old list
courses_0 = ['English', 'French']
courses.extend(courses_0)
print('2----------------extend------------------\n' + str(courses))

# ---------->> insert an item to specific location in the list,
# insert 'Art' to position 0 in the list, and shift next items
courses.insert(0, 'Chemistry')
print('3-----------------insert item at specific location-----------------\n' + str(courses))


# ---------->> insert a list of multiple values into another list (Extend the list)
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print('4------------------insert list----------------\n' + str(courses))

courses_3 = ['Philosphy', 'Arabic']
courses.insert(2, courses_2+courses_3)
print('5----------------insert concatenated lists------------------\n' + str(courses))

# ---------->> remove an item from the list
courses.remove('Math')
print('6-------------remove Math item---------------------\n' + str(courses))

courses.remove('Art')  # remove Art as an item, but not from the internal lists
print('7---------------remove Art item--------------------\n' + str(courses))

# ---------->> pop an item from the list
# remove last item from the list and return it to a variable , like a stack pop
popped = courses.pop()
print('8------------------pop last item----------------\n' + str(courses))
print('9------------------poped item----------------\n' + str(popped))
# save a copy of the list
courses_origin = courses

# ---------->> reverse the list elements, last item become the first ,..
courses.reverse()
print('10--------------------reversed list--------------\n' + str(courses))

# ---------->> sort the list string elements in alphabitical (Ascending/decsending) order in same list
courses.sort()
print('11--------------------alphapitical sorted list--------------\n' + str(courses))

courses[1].sort()
print('12--------------------sorted inner list--------------\n' + str(courses))

nums = [1, 5, 2, 4, 2, 3]
nums.sort()
print('13--------------------Ascending sort for list of numbers-------------\n' + str(nums))


nums = [1, 5, 2.3, 4, -3.6, 2, 3, 0]
nums.sort()
print('14--------------------Ascending sort for list of float numbers-------------\n' + str(nums))

nums.sort(reverse=True)
print('15--------------------Descending sort for list of float numbers-------------\n' + str(nums))
courses.sort(reverse=True)
print('16--------------------Descending sort for list of float numbers-------------\n' + str(courses))

# -------->> sort the list without changing it
sorted_courses = sorted(courses_origin)
print('17--------------------sorted list -------------\n' +
      str(sorted_courses))
print('18--------------------original list without change-------------\n' +
      str(courses))

# --------List tools for Numbers----------------------#
# -------->> min number in list
print('19--------------------min num in list -------------\n' +
      '======> ' + str(min(nums)))
# -------->> max number in list
print('20--------------------max num in list -------------\n' +
      '======>  ' + str(max(nums)))
# -------->> sum of list numbers
print('21--------------------Sum of nums in list --------------\n' +
      '======>' + str(sum(nums)))

# -------- define the index of certain value ----------------#
print('22--------------------index of certain value --------------\n' +
      str(courses.index('Physics')) + '\n' +
      str(courses.index('History')) + '\n' +
      str(courses.index('Chemistry')) + '\n' +
      str(courses[5].index('Art')) + '\n'




      )

# -------- check if item in the list ----------------#
print('23--------------------Check if item in list --------------\n')
print('Math' in courses_origin)
print('History' in courses_origin)

# to print all list items through loop
print('24-------------------- loop on list items--------------\n')
i = 0
for item in courses_origin:
    print(str(i) + ' - ' + str(item))
    i = i+1````
# Another way to show the index of each course using enumerate function, it return two values
print('\n25-------------------- better way to loop on list items--------------\n')
for index, item in enumerate(courses_origin, start=1):
    print(index, item)

# to join the list items with comma separate| or Hyphen
print('\n26--------------------join list items with certain opertor--------------\n')
course_str = ' - '.join(courses_origin[0])
print(course_str)
course_str1 = ' - '.join(courses_origin[5])
print(course_str1)

# to retrieve the joined list items and split it back to a list of items
print('\n26--------------------Split the joined list and get it back--------------\n')
course_str = course_str.split(' - ')
print(course_str)
course_str1 = course_str1.split(' - ')
print(course_str1)



# -------------------Tuples--------------#
# Tuples is very similar to the list but with the fact that you cant change the tuples, its like constant values of items
# Tuples are immutable, while lists are mutable
