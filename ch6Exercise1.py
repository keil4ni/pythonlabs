# Keilani Li
'''The following coding program shows 2 lists of friends made in 2017 and 2018 and asks for user to
enter their own friend name so these two lists can be compared. The user can then add a new friend to
the 2017 or 2018 friend list'''

friends_2017 = ["Mikyla", "Fabian"]
friends_2018 = ["Aimee", "Normandy"]
allFriends = friends_2017 + friends_2018

print('List of friends:', allFriends)

enterFriend = input('Please enter the name of a friend: ')

if enterFriend in friends_2017:
    print('Keilani found this friend in 2017!\n')
elif enterFriend in friends_2018:
    print('Keilani found this friend in 2018!\n')
else:
    print('Keilani is not friends with this person.\n')

newFriend = input('Please enter the name of a friend you want to add: ')
friendYear = int(input('Did you meet this friend in 2017 or 2018? '))

if friendYear == 2017:
    friends_2017.append(newFriend)
elif friendYear == 2018:
    friends_2018.append(newFriend)

print('\nFriends met in 2017:', friends_2017)
print('Friends met in 2018:', friends_2018)

'''
List of friends: ['Mikyla', 'Fabian', 'Aimee', 'Normandy']
Please enter the name of a friend: Fabian
Keilani found this friend in 2017!

Please enter the name of a friend you want to add: Jason
Did you meet this friend in 2017 or 2018? 2017

Friends met in 2017: ['Mikyla', 'Fabian', 'Jason']
Friends met in 2018: ['Aimee', 'Normandy']

Process finished with exit code 0
'''

'''
List of friends: ['Mikyla', 'Fabian', 'Aimee', 'Normandy']
Please enter the name of a friend: Kyle
Keilani is not friends with this person.

Please enter the name of a friend you want to add: Kyle
Did you meet this friend in 2017 or 2018? 2018

Friends met in 2017: ['Mikyla', 'Fabian']
Friends met in 2018: ['Aimee', 'Normandy', 'Kyle']

Process finished with exit code 0
'''
