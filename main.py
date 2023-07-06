# Keilani Li
'''The following coding program prompts the user for hours and rate per hour to calculate their gross pay.
If the employee has worked more than 40 hours, the extra hours worked will receive 1.5 times their hourly rate'''
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if (hours <= 40):
    total = hours * rate
elif (hours > 40):
    total = (40 * rate) + ((hours - 40) * (rate * 1.5))
    # 40 hours of work receives the normal hourly rate
    # the number of hours worked after 40 hours will receive 1.5 times their hourly rate

print('\n\nPay: ', total)

'''
Enter Hours: 50
Enter Rate: 13


Pay:  715.0

Process finished with exit code 0
'''

'''
Enter Hours: 28
Enter Rate: 16.50


Pay:  462.0

Process finished with exit code 0
'''