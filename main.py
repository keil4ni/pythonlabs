# Keilani Li
'''The following coding program prompts the user for the number of hours worked and their hourly pay to calculate
their gross pay. It also uses 3 functions'''

def get_input():
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    return hours, rate

def compute_pay(hours, rate):
    if (hours <= 40):
        total = hours * rate
    elif (hours > 40):
        total = (40 * rate) + ((hours -40) * (rate * 1.5))
    return total

def print_output(total):
    print('Pay:', total)

def main():
    hours, rate = get_input()
    total = compute_pay(hours, rate)
    print_output(total)

main()

'''
Enter Hours: 20
Enter Rate: 14.5
Pay: 290.0

Process finished with exit code 0
'''

'''
Enter Hours: 42
Enter Rate: 19.15
Pay: 823.45

Process finished with exit code 0
'''