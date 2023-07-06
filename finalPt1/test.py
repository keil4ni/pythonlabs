from main import Order, Student, Staff

if  __name__ == "__main__":
    print('Welcome to the De Anza Food Court!')
    flag = True
    while flag:
        user = input('Are you a student? (Y/N) ')
        if user.upper() == 'Y':
            student = Student()
            student.displayMenu()
            student.get_inputs() # allows the user to create their order

            print('Here is your order so far:\n')
            student.compute_bill()
            student.print_bill() # allows the user to view their order before payment

            student.update_inputs() # allows the user to update their order before payment
            student.delete_inputs() # allows the user to delete items from their order before payment

            student.compute_bill()
            student.print_bill()
            student.saveToFile() # the final bill is computed and saved into the system
        elif user.upper() == "N":
            staff = Staff()
            staff.displayMenu()
            staff.get_inputs()

            print('Here is your order so far:\n')
            staff.compute_bill()
            staff.print_bill() # allows the user to view their order before payment

            staff.update_inputs() # allows the user to update their order before payment
            staff.delete_inputs() # allows the user to delete items from their order before payment

            staff.compute_bill()
            staff.print_bill()
            staff.saveToFile() # the final bill is computed and saved into the system
        else:
            print('Error, please enter Y or N.')
            continue

        userInputToContinue = input("\nWould you like to place another order? (Any keys = Yes, N = No) ")

        if userInputToContinue.upper() == 'N':
            print("Thank you for ordering! The system will now shut down.")
            flag = False