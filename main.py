# Keilani Li
'''The following coding program prompts the user for their company name, number of hours worked and their hourly
pay to calculate their gross pay. It checks for invalid inputs (string inputs, negative numbers) and outputs a
random number between 1000 to 2000 for their document numbers'''

import random
def get_input():
    companyName = input('Enter your company name: ')

    while True:
        try:
            hours = float(input('Enter Hours: '))
            if (hours < 0):
                continue

            rate = float(input('Enter Rate: '))
            if (rate < 0):
                continue
        except:
            print('Error, please enter numeric value')
        else:
            break
    return companyName, hours, rate

def compute_pay(hours, rate):
    if (hours <= 40):
        total = hours * rate
    elif (hours > 40):
        total = (40 * rate) + ((hours -40) * (rate * 1.5))
    return total

def print_output(companyName, hours, rate, total):
    print('\n\nCompany:', companyName)
    print('Hours:', hours)
    print('Rate:', rate)
    print('Pay:', total)

    documentNumber = random.randint(1000, 2000)
    print('\nYour document number is:', documentNumber)
    print('Your', companyName, 'gross pay is:', round(total, 2), 'dollars.')

def main():
    companyName, hours, rate = get_input()
    total = compute_pay(hours, rate)
    print_output(companyName, hours, rate, total)

main()

'''
Enter your company name: Amazon
Enter Hours: 42
Enter Rate: 35.2


Company: Amazon
Hours: 42.0
Rate: 35.2
Pay: 1513.6

Your document number is: 1610
Your Amazon gross pay is: 1513.6 dollars.

Process finished with exit code 0
'''

'''
Enter your company name: Safeway
Enter Hours: test
Error, please enter numeric value
Enter Hours: -1
Enter Hours: 27
Enter Rate: 14.5


Company: Safeway
Hours: 27.0
Rate: 14.5
Pay: 391.5

Your document number is: 1115
Your Safeway gross pay is: 391.5 dollars.

Process finished with exit code 0
'''