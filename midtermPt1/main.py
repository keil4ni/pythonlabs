# Dream Team: Keilani Li & Azel Lalli
'''The following program is menu-driven for the De Anza College Food Court. It uses 4 functions and 1 main function
that helps the user select their menu item and calculate their total'''

def displayMenu(): # displays burger menu from the De Anza College Food Court with their respective prices
    print('(1) De Anza Burger -- $5.25')
    print('(2) Bacon Cheese -- $5.75')
    print('(3) Mushroom Swiss -- $5.95')
    print('(4) Western Burger -- $5.95')
    print('(5) Don Cali Burger -- $5.95')
    print('(6) Exit')

def get_inputs():
    '''gets user's food selection, quantity input, and asks if they are a student or staff member for tax calculation.
    if the user enters 6 as their first input, it will end the program. if the user enters 6 after making a selection,
    their bill will be calculated in the next function. all inputs are checked through try/except blocks in case
    user enters a string, negative value, or an option that isn't on the menu'''
    itemList = []
    quantityList = []

    while True:
        try:
            item = int(input('Select a number from 1-5 or press 6 to exit: '))
        except:
            print('Error, please enter numeric value.')
        else:
            if item > 6 or item < 1:
                print('Invalid selection, please try again.')
                continue
            elif (item != 6):
                quantity1 = int(input('Quantity: '))
                itemList.append(item)
                quantityList.append(quantity1)
                break
            elif (item == 6):
                print('Thank you, hope to see you again!')
                exit()

    while True:
        try:
            otherItems = int(input('Select a number from 1-5 or press 6 to exit: '))
            if otherItems >= 1 and otherItems < 6:
                itemList.append(otherItems)
                otherQuantity = int(input('Quantity: '))
                quantityList.append(otherQuantity)
            if otherItems > 6 or otherItems < 1:
                print('Invalid selection, please try again.')
                continue
            if otherItems == 6:
                break
        except:
            print('Error, please enter numeric value.')
        else:
            continue

    while otherItems == 6:
        tax = input('Are you a student? (Y/N) ')
        if tax == 'Y' or tax == 'y':
            tax = 0
            break
        elif tax == 'N' or tax == 'n':
            tax = 0.09
            break
        else:
            print('Error, please enter Y or N.')
            continue

    return itemList, quantityList, tax

def compute_bill(itemList, quantityList, tax):
    '''function converts user's option numbers into food item names, calculates the cost of each item based on quantity,
    and calculates the subtotal, tax amount, and grand total'''

    itemCosts = []

    for item in range(len(itemList)):
        if itemList[item] == 1:
            itemList[item] = 'De Anza Burger'
            itemCosts.append(5.25)

        if itemList[item] == 2:
            itemList[item] = 'Bacon Cheese'
            itemCosts.append(5.75)

        if itemList[item] == 3:
            itemList[item] = 'Mushroom Swiss'
            itemCosts.append(5.95)

        if itemList[item] == 4:
            itemList[item] = 'Western Burger'
            itemCosts.append(5.95)

        if itemList[item] == 5:
            itemList[item] = 'Don Cali Burger'
            itemCosts.append(5.95)

    itemTotals = [itemCosts[i] * quantityList[i] for i in range(len(itemCosts))] # multiplies each item by quantity amount using list comprehension

    subtotal = sum(itemCosts) # sum() function adds all numbers in list
    taxAmount = subtotal * tax
    grandTotal = subtotal + taxAmount

    return itemList, itemCosts, subtotal, taxAmount, grandTotal

def print_bill(itemList, itemCosts, quantityList, subtotal, taxAmount, grandTotal):
    '''this function displays the bill to user which includes food items, quantities, costs of each item,
    total before tax (subtotal), tax amount, and total after tax'''

    print('\t\t\tRECEIPT')
    print('QTY\t\t ITEM\t\t\t\t COST')
    for item, quantity, cost in zip(itemList, quantityList, itemCosts):
        print('{:3.0f}'.format(quantity), '\t', item.ljust(15), '{:8.2f}'.format(cost))

    print('\n\nSUBTOTAL\t\t\t\t', '{:8.2f}'.format(subtotal))
    print('TAX\t\t\t\t\t\t', '{:8.2f}'.format(taxAmount))
    print('TOTAL\t\t\t\t\t', '{:8.2f}'.format(grandTotal))

def main(): # this function runs the entire program using all functions defined above
    displayMenu()
    itemList, quantityList, tax = get_inputs()
    itemList, itemCosts, subtotal, taxAmount, grandTotal = compute_bill(itemList, quantityList, tax)
    print_bill(itemList, itemCosts, quantityList, subtotal, taxAmount, grandTotal)

main()

'''
(1) De Anza Burger -- $5.25
(2) Bacon Cheese -- $5.75
(3) Mushroom Swiss -- $5.95
(4) Western Burger -- $5.95
(5) Don Cali Burger -- $5.95
(6) Exit
Select a number from 1-5 or press 6 to exit: 1
Quantity: 5
Select a number from 1-5 or press 6 to exit: 2
Quantity: 3
Select a number from 1-5 or press 6 to exit: 5
Quantity: 1
Select a number from 1-5 or press 6 to exit: 3
Quantity: 2
Select a number from 1-5 or press 6 to exit: 6
Are you a student? (Y/N) y
			RECEIPT
QTY		 ITEM				 COST
  5 	 De Anza Burger      5.25
  3 	 Bacon Cheese        5.75
  1 	 Don Cali Burger     5.95
  2 	 Mushroom Swiss      5.95


SUBTOTAL				    22.90
TAX						     0.00
TOTAL					    22.90

Process finished with exit code 0
'''

'''
(1) De Anza Burger -- $5.25
(2) Bacon Cheese -- $5.75
(3) Mushroom Swiss -- $5.95
(4) Western Burger -- $5.95
(5) Don Cali Burger -- $5.95
(6) Exit
Select a number from 1-5 or press 6 to exit: 3
Quantity: 20
Select a number from 1-5 or press 6 to exit: 1
Quantity: 1
Select a number from 1-5 or press 6 to exit: 7
Invalid selection, please try again.
Select a number from 1-5 or press 6 to exit: 0
Invalid selection, please try again.
Select a number from 1-5 or press 6 to exit: 6
Are you a student? (Y/N) N
			RECEIPT
QTY		 ITEM				 COST
 20 	 Mushroom Swiss      5.95
  1 	 De Anza Burger      5.25


SUBTOTAL				    11.20
TAX						     1.01
TOTAL					    12.21

Process finished with exit code 0
'''
