# Keilani Li
# The following coding program calculates the sum of digits of an input number

number = (input('Enter integer: '))

if number.isdigit():
    index = 0
    total = 0
    while index < len(number):
        total += int(number[index])
        index += 1
    print('Sum:', total)
else:
    print('Error, please enter numeric value')

'''
Enter integer: 2385
Sum: 18

Process finished with exit code 0
'''

'''
Enter integer: 1946
Sum: 20

Process finished with exit code 0
'''

'''
Enter integer: 7789
Sum: 31

Process finished with exit code 0
'''