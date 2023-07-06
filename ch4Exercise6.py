# Keilani Li
# The following coding program pro mpts user for an email address, verifies if it's valid, then outputs its domain name

emailAddress = input("Enter email address: ")

if "@" and "." in emailAddress:
    atIndex = emailAddress.find("@") # finds index of "@"
    periodIndex = emailAddress.find(".") # finds index of "."

    print("Domain name:", emailAddress[atIndex + 1 : periodIndex])
    '''slices string using colon operator starting from the index after the "@"
    up to but not including "." to get domain name'''

'''
Enter email address: 20522938@fhda.edu
Domain name: fhda

Process finished with exit code 0
'''

'''
Enter email address: keilanili@gmail.com
Domain name: gmail

Process finished with exit code 0
'''

'''
Enter email address: exampleinput@outlook.com
Domain name: outlook

Process finished with exit code 0
'''
