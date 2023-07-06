# Keilani Li
'''The following coding program prompts the user for hours and rate per hour to calculate their gross pay.
If the employee has worked more than 40 hours, the extra hours worked will receive 1.5 times their hourly rate'''
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
else:
    if (hours <= 40):
        total = hours * rate
    elif (hours > 40):
        total = (40 * rate) + ((hours - 40) * (rate * 1.5))
        # 40 hours of work receives the normal hourly rate
        # the number of hours worked after 40 hours will receive 1.5 times their hourly rate
    print('\n\nPay: ', total)

'''
Enter Hours: 30
Enter Rate: seventeen
Error, please enter numeric input

Process finished with exit code 0
'''

'''
Enter Hours: twenty one
Error, please enter numeric input

Process finished with exit code 0
'''

'''
Enter Hours: 41
Enter Rate: 15.50


Pay:  643.25

Process finished with exit code 0
'''
