# Keilani Li
'''The following coding program prompts the user for their company name, hours, and rate per hour to calculate their gross pay.
If the employee has worked more than 40 hours, the extra hours worked will receive 1.5 times their hourly rate.
The code will validate user's inputs in a loop and generate a random number between 1000-2000 for their document numbers.'''
import random # needed for randint() function

companyName = input('Enter Company Name: ')

while True:
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

        print('\n\nCompany:', companyName)
        print('Hours:', hours)
        print('Rate:', rate)

        documentNumber = random.randint(1000, 2000) # generates random number between 1000 and 2000
        print('\nYour document number is:', documentNumber)
        print('Your', companyName, 'gross pay is:', round(total, 2), 'dollars.')
        break

'''
Enter Company Name: Amazon
Enter Hours: 46
Enter Rate: 35.25


Company: Amazon
Hours: 46.0
Rate: 35.25

Your document number is: 1264
Your Amazon gross pay is: 1727.25 dollars.

Process finished with exit code 0
'''

'''
Enter Company Name: Safeway
Enter Hours: 2u
Error, please enter numeric input
Enter Hours: 28
Enter Rate: 15.5-
Error, please enter numeric input
Enter Hours: 28
Enter Rate: 15.5


Company: Safeway
Hours: 28.0
Rate: 15.5

Your document number is: 1916
Your Safeway gross pay is: 434.0 dollars.

Process finished with exit code 0
'''

'''
Enter Company Name: Chick-fil-A
Enter Hours: 32
Enter Rate: 16.;
Error, please enter numeric input
Enter Hours: 32
Enter Rate: 16.15


Company: Chick-fil-A
Hours: 32.0
Rate: 16.15

Your document number is: 1712
Your Chick-fil-A gross pay is: 516.8 dollars.

Process finished with exit code 0
'''