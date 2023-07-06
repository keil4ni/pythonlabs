# Dream Team: Keilani Li & Azel Lalli
'''The following program is menu-driven for the De Anza College Food Court. It uses functions, classes, and dictionaries
to help the user select their menu item and calculate their total'''

class Order(): # this is a superclass that contains functions that help the customer place their order
    def __init__(self): # defines instance variables for the class
        self._subtotal = 0.0
        self._total = 0.0

        self._priceDict = {"De Anza Burger" : 5.25, "Bacon Cheese" : 7.75, "Mushroom Swiss" : 5.95,
                           "Western Burger" : 5.95, "Don Cali Burger" : 5.95}
        self._orderDict = {"De Anza Burger" : 0, "Bacon Cheese" : 0, "Mushroom Swiss" : 0,
                           "Western Burger" : 0, "Don Cali Burger" : 0}

    def displayMenu(self): # displays burger menu from the De Anza College Food Court with their respective prices
        print('DE ANZA FOOD COURT BURGER OPTIONS')
        number = 1
        for option in self._priceDict:
            print('({a}) {b:15s} {c:8.2f}'.format(a = number, b = option, c = self._priceDict[option]))
            number += 1
        print('(6) Exit')

    def get_inputs(self):
        '''gets user's food selection and quantity input. if the user enters 6 as their first input, it will end the
        program. if the user enters 6 after making a selection, their bill will be calculated and outputted onto the screen.
        all inputs are saved in dictionaries and are checked through try/except blocks in case the user enters a string,
        a negative value, or an option that isn't on the menu'''
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
                    if item == 1:
                        self._orderDict["De Anza Burger"] = quantity1
                    if item == 2:
                        self._orderDict["Bacon Cheese"] = quantity1
                    if item == 3:
                        self._orderDict["Mushroom Swiss"] = quantity1
                    if item == 4:
                        self._orderDict["Western Burger"] = quantity1
                    if item == 5:
                        self._orderDict["Don Cali Burger"] = quantity1
                    break
                elif (item == 6):
                    print('Thank you, hope to see you again!')
                    exit()

        while True:
            try:
                item2 = int(input('Select a number from 1-5 or press 6 to exit: '))
                if item2 > 6 or item2 < 1:
                    print('Invalid selection, please try again.')
                    continue
                elif (item2 != 6):
                    quantity2 = int(input('Quantity: '))
                    if item2 == 1:
                        self._orderDict["De Anza Burger"] = quantity2
                    if item2 == 2:
                        self._orderDict["Bacon Cheese"] = quantity2
                    if item2 == 3:
                        self._orderDict["Mushroom Swiss"] = quantity2
                    if item2 == 4:
                        self._orderDict["Western Burger"] = quantity2
                    if item2 == 5:
                        self._orderDict["Don Cali Burger"] = quantity2
                elif (item2 == 6):
                    break
            except:
                print('Error, please enter numeric value')
            else:
                continue

    def compute_bill(self):
        '''this function calculates the user's subtotal, tax amount, and grand total'''

        for burger in self._priceDict:
            self._subtotal += self._orderDict[burger] * self._priceDict[burger]
            self._total = self._subtotal + (self._subtotal * self._tax)

    def print_bill(self):
        '''this function displays the bill to the user which includes food items, quantities, costs of each item,
        subtotal, tax amount, and the grand total after tax'''

        print('\t\t\tRECEIPT')
        print('QTY\t\tITEM\t\t\t\t COST')
        for burger in self._orderDict:
            print('%-7d %-20s $%-8.2f' % (self._orderDict[burger], burger, (self._orderDict[burger] * self._priceDict[burger])))

        print('\n\nSUBTOTAL\t\t\t\t', '{:8.2f}'.format(self._subtotal))
        print('TAX\t\t\t\t\t\t', '{:8.2f}'.format(self._tax))
        print('TOTAL\t\t\t\t\t', '{:8.2f}'.format(self._total))

    def saveToFile(self):
        '''this function saves the bill information and writes it into a txt file'''
        import time
        import datetime

        orderTime = time.time()
        orderTimeStamp = datetime.datetime.fromtimestamp(orderTime).strftime('%Y-%m-%d %H-%M-%S')
        orderTimeStamp = orderTimeStamp + '.txt'

        billFile = open(orderTimeStamp, 'w')
        billFile.write('\t\t\tRECEIPT\n')
        billFile.write('QTY\t\tITEM\t\t\t\t COST\n')
        for burger in self._orderDict:
            billFile.write('%-7d %-20s $%-8.2f\n' % (self._orderDict[burger], burger, (self._orderDict[burger] * self._priceDict[burger])))
        billFile.write('\n\nSUBTOTAL\t\t\t\t %-8.2f\n' % (self._subtotal))
        billFile.write('TAX\t\t\t\t\t\t %-8.2f\n' % (self._tax))
        billFile.write('TOTAL\t\t\t\t\t %-8.2f\n' % (self._total))

        billFile.close()

    def update_inputs(self):
        '''this function allows the user to update the quantity of the burger(s) they chose before their order is finalized'''
        x = True
        while x:
            updateInput = input('Is there anything you want to update before confirming your order? (Y/N) ')
            if updateInput.upper() == 'Y':
                while True:
                    try:
                        updateItem = int(input('Select the burger number you want to update the quantity for. Press 6 to exit. '))
                        if updateItem > 6 or updateItem < 1:
                            print('Invalid selection, please try again.')
                            continue
                        elif (updateItem != 6):
                            updateQuantity = int(input('Quantity: '))
                            if updateItem == 1:
                                self._orderDict["De Anza Burger"] = updateQuantity
                            if updateItem == 2:
                                self._orderDict["Bacon Cheese"] = updateQuantity
                            if updateItem == 3:
                                self._orderDict["Mushroom Swiss"] = updateQuantity
                            if updateItem == 4:
                                self._orderDict["Western Burger"] = updateQuantity
                            if updateItem == 5:
                                self._orderDict["Don Cali Burger"] = updateQuantity
                        elif (updateItem == 6):
                            x = False
                            break
                    except:
                        print('Error, please enter numeric value')
                    else:
                        continue
            elif updateInput.upper() == 'N':
                break
            else:
                print('Error, please enter Y or N.')
                continue

    def delete_inputs(self):
        '''this function deletes the user's inputs by changing the specific burger's quantity to 0 before their order
        is finalized'''
        x = True
        while x:
            deleteInput = input('Is there anything you want to delete from your order? (Y/N) ')
            if deleteInput.upper() == 'Y':
                while True:
                    try:
                        deleteItem = int(input('Select the burger number you want to delete. Press 6 to exit. '))
                        if deleteItem > 6 or deleteItem < 1:
                            print('Invalid selection, please try again.')
                            continue
                        elif (deleteItem != 6):
                            if deleteItem == 1:
                                self._orderDict["De Anza Burger"] = 0
                                print('Successfully deleted De Anza Burger.')
                            if deleteItem == 2:
                                self._orderDict["Bacon Cheese"] = 0
                                print('Successfully deleted Bacon Cheese Burger.')
                            if deleteItem == 3:
                                self._orderDict["Mushroom Swiss"] = 0
                                print('Successfully deleted Mushroom Swiss.')
                            if deleteItem == 4:
                                self._orderDict["Western Burger"] = 0
                                print('Successfully deleted Western Burger.')
                            if deleteItem == 5:
                                self._orderDict["Don Cali Burger"] = 0
                                print('Successfully deleted Don Cali Burger.')
                        elif (deleteItem == 6):
                            x = False
                            break
                    except:
                        print('Error, please enter numeric value')
                    else:
                        continue
            elif deleteInput.upper() == 'N':
                break
            else:
                print('Error, please enter Y or N.')
                continue

class Student(Order):
    '''this is a subclass that inherits instance variables and functions from the superclass. when this
    class is used, the user will not be charged for tax when they finish placing their order'''
    def __init__(self): # calls instance variables from the superclass and has its own instance variable of no tax
        super().__init__()
        self._tax = 0.0

class Staff(Order):
    '''this is a subclass that inherits instance variables and functions from the superclass. when this
    class is used, the user will be charged 9% tax when they finish placing their order'''
    def __init__(self): # calls instance variables from the superclass and has its own instance variable of 9% tax
        super().__init__()
        self._tax = 0.09
