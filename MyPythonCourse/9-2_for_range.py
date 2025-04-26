# range() function is used to generate a sequence of numbers.
# It's commonly used in loops to iterate over a certain range of values. 

# The general syntax of the range(start, stop[, step])
# start: The starting value of the sequence (inclusive). If not specified, it defaults to 0.
# stop: The end value of the sequence (exclusive).
# step: The increment between each number in the sequence. If not specified, it defaults to 1.

print(range(1,10))  # This is wrong
print('------------------')

sum(range(4))  # 0 + 1 + 2 + 3
print('------------------')

for i in range(5):
    print(i)
print('------------------')

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
print('------------------')

