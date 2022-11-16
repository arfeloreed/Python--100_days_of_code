# adding even numbers

# set a default value for total of even numbers
total_of_even = 0

# calculate the total of even numbers from 1 - 100

# for even_number in range(2, 101, 2):  I can also use this
for even_number in range(0, 101, 2):
    total_of_even += even_number

print(total_of_even)

# using another solution

# for even_number in range(1, 101):
#     if even_number % 2 == 0:
#         total_of_even += even_number

# print(total_of_even)
