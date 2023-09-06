# **********Part 1**********

letter_a = "A"
three_spaces = "   "

print((three_spaces*5) + letter_a)
print((three_spaces * 4) + letter_a + (three_spaces *2) + letter_a) 
print((three_spaces * 4) + (letter_a * 7))
print((three_spaces *3) + letter_a + (three_spaces *4) + letter_a)
print((three_spaces *2) + letter_a + (three_spaces *6) + letter_a)



# **********Part 2**********

num1 = 100
num2 = 3.14159

print(f'{num1} multiplied by {num2} = {num1 * num2}')
print(f'The type of {num1} is {type(num1)}')
print(f'The type of {num2} is {type(num2)}')
print(f'The unique object identifier of {num1} is {id(num1)}')
print(f'The unique object identifier of {num2} is {id(num2)}')



# **********Part 3**********

string1 = "Hello"
string2 = "Hello"

print(f'Is string1- {string1}, the same as string2- {string2}')
print(f'string1 is of type {type(string1)}, and id of {id(string1)}')
print(f'string2 is of type {type(string2)}, and id of {id(string2)}')
if id(string1) == id(string2):
    print('Yes! They are the same')
else:
    print('NO, they are NOT the same')

string1 = string1 + " There"
string2 = string2 + " There"

print(f'Is string1- {string1}, the same as string2- {string2}')
print(f'string1 is of type {type(string1)}, and id of {id(string1)}')
print(f'string2 is of type {type(string2)}, and id of {id(string2)}')
print('NO, they are NOT the same')




num1 = 10
num2 = 10.0

print(f'num1 = {num1}, type of {type(num1)}, id of {id(num1)}')
print(f'num2 = {num2}, type of {type(num2)}, id of {id(num2)}')

# Verify that Python assigns a different object reference to
# num1 and num2 than it had before the arithmetic
num1 = num1 + 100
num2 = num2 - 5

print(f'Now num1 = {num1}, type of {type(num1)}, id of {id(num1)}')
print(f'And num2 = {num2}, type of {type(num2)}, id of {id(num2)}')

