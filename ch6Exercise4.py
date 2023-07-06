# Keilani Li
'''The following coding program creates a table of medals belonging to their respective country. If a country
doesn't have any gold medals, they will be removed from the table.'''

countryMedals = [
    ('Canada', 0, 3, 0),
    ('Italy', 0, 0, 1),
    ('Germany', 0, 0, 1),
    ('Japan', 1, 0, 0),
    ('Russia', 3, 1, 1),
    ('South Korea', 0, 1, 0),
    ('United States', 1, 0, 1)
]

for medal in countryMedals: # prints table
    print('%s has %d gold, %d silver, and %d bronze medals.' % medal)

total = sum(medal[1] + medal[2] + medal[3] for medal in countryMedals) # calculates total number of medals in table
print('\nTotal medals:', total)

totalGold = sum(medal[1] for medal in countryMedals) # calculates total number of gold medals in table
print('Total gold medals:', totalGold)

totalSilver = sum(medal[2] for medal in countryMedals) # calculates total number of silver medals in table
print('Total silver medals:', totalSilver)

totalBronze = sum(medal[3] for medal in countryMedals) # calculates total number of bronze medals in table
print('Total bronze medals:', totalBronze)

countryMedals = list(filter(lambda x : x[1] > 0, countryMedals)) # removes countries without gold medals using filter function
print('\nThe following countries have gold medals:')
for medal in countryMedals:
    print('%s has %d gold, %d silver, and %d bronze medals.' % medal)

medalDict = {}
for medal in countryMedals: # saves countries with gold medals in a dictionary
    medalDict[medal[0]] = list((medal[1], medal[2], medal[3]))
print('\nThe following dictionary saved countries with gold medals:')
print(medalDict)

'''
Canada has 0 gold, 3 silver, and 0 bronze medals.
Italy has 0 gold, 0 silver, and 1 bronze medals.
Germany has 0 gold, 0 silver, and 1 bronze medals.
Japan has 1 gold, 0 silver, and 0 bronze medals.
Russia has 3 gold, 1 silver, and 1 bronze medals.
South Korea has 0 gold, 1 silver, and 0 bronze medals.
United States has 1 gold, 0 silver, and 1 bronze medals.

Total medals: 14
Total gold medals: 5
Total silver medals: 5
Total bronze medals: 4

The following countries have gold medals:
Japan has 1 gold, 0 silver, and 0 bronze medals.
Russia has 3 gold, 1 silver, and 1 bronze medals.
United States has 1 gold, 0 silver, and 1 bronze medals.

The following dictionary saved countries with gold medals:
{'Japan': [1, 0, 0], 'Russia': [3, 1, 1], 'United States': [1, 0, 1]}

Process finished with exit code 0
'''
