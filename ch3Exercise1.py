# Keilani Li
# This coding program prompts the user for a size and compares it to the number 10

size = float(input('Enter size: '))

if size < 10:
    print('Smaller')
elif size > 10:
    print('Bigger')
else:
    print('Fit')

print('Finish')

'''
Enter size: 2
Smaller
Finish

Process finished with exit code 0
'''

'''
Enter size: 14
Bigger
Finish

Process finished with exit code 0
'''

'''
Enter size: 10
Fit
Finish

Process finished with exit code 0
'''
