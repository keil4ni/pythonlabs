# Keilani Li
'''The following coding program asks for the user's company so it can be validated in the database list. If the user
enters an invalid input, the list of companies will be shown. Then, their pay (including overtime) will be calculated
and outputted.'''

COMPANYLIST = ["Amazon", "Apple", "Facebook", "Google", "Uber"]

def get_inputs():
    theDict = dict()

    companyName = input('Enter company name: ')
    if companyName not in COMPANYLIST:
        print('Invalid input, please try again.')
        companyName = input('Enter company name: ')
        if companyName not in COMPANYLIST:
            print('Sorry, your company is not listed in the database.')
            print('List of companies:', COMPANYLIST, '\n')
    theDict['company_name'] = companyName

    while True:
        try:
            hours = float(input('Enter Hours: '))
            if hours <= 0:
                continue
            else:
                theDict['hours'] = hours

            rate = float(input('Enter Rate: '))
            if rate <= 0:
                continue
            else:
                theDict['rate'] = rate
        except:
            print('Error, please enter numeric value')
        else:
            break
    return theDict

def compute_pay(theDict):
    if theDict['hours'] <= 40:
        total = theDict['hours'] * theDict['rate']
    elif theDict['hours'] > 40:
        total = (40 * theDict['rate']) + ((theDict['hours'] - 40) * (theDict['rate'] * 1.5))

    theDict['total'] = round(total, 2)
    return theDict

def print_output(theDict):
    print('\nCompany:', theDict['company_name'])
    print('Hours:', theDict['hours'])
    print('Rate:', theDict['rate'])
    print('Pay:', theDict['total'])

def payProcess():
    theDict = get_inputs()
    theDict = compute_pay(theDict)
    print_output(theDict)

payProcess()

'''
Enter company name: Google
Enter Hours: 36
Enter Rate: 40.15

Company: Google
Hours: 36.0
Rate: 40.15
Pay: 1445.4

Process finished with exit code 0
'''

'''
Enter company name: Starbucks
Invalid input, please try again.
Enter company name: Starbucks
Sorry, your company is not listed in the database.
List of companies: ['Amazon', 'Apple', 'Facebook', 'Google', 'Uber'] 

Enter Hours: 41
Enter Rate: 13.3

Company: Starbucks
Hours: 41.0
Rate: 13.3
Pay: 551.95

Process finished with exit code 0
'''
