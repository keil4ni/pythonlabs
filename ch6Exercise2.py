# Keilani Li
'''The following coding program uses dictionaries to compare my list of friends in 2017 and 2018
to the user's friend lists. The user can then add a new friend to the 2017 or 2018 friend dictionary.'''

friends_dict = {2017: ["Mikyla", "Fabian"], 2018: ["Aimee", "Normandy"]}
allFriends = friends_dict[2017] + friends_dict[2018]
print('All friends:', allFriends)

enterFriend = input('Please enter the name of a friend: ')

for friend in friends_dict[2017]:
    if enterFriend == friend:
        print('Keilani found this friend in 2017!\n')
for friend in friends_dict[2018]:
    if enterFriend == friend:
        print('Keilani found this friend in 2018!\n')

newFriend = input('Please enter the name of a friend you want to add: ')
friendYear = int(input('Did you meet this friend in 2017 or 2018? '))

if friendYear == 2017:
    friends_dict[2017].append(newFriend)
elif friendYear == 2018:
    friends_dict[2018].append(newFriend)

print('\nFriends met in 2017:', friends_dict[2017])
print('Friends met in 2018:', friends_dict[2018])

'''
All friends: ['Mikyla', 'Fabian', 'Aimee', 'Normandy']
Please enter the name of a friend: Mikyla
Keilani found this friend in 2017!

Please enter the name of a friend you want to add: Tommy
Did you meet this friend in 2017 or 2018? 2018

Friends met in 2017: ['Mikyla', 'Fabian']
Friends met in 2018: ['Aimee', 'Normandy', 'Tommy']

Process finished with exit code 0
'''

'''
All friends: ['Mikyla', 'Fabian', 'Aimee', 'Normandy']
Please enter the name of a friend: Normandy
Keilani found this friend in 2018!

Please enter the name of a friend you want to add: John
Did you meet this friend in 2017 or 2018? 2017

Friends met in 2017: ['Mikyla', 'Fabian', 'John']
Friends met in 2018: ['Aimee', 'Normandy']

Process finished with exit code 0
'''
