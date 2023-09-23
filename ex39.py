# create a mapping of state to abbrevition 
states = {'Oregon' : 'OR','Florida' : 'FL' , 'California' : 'CA' , 'New York' : 'NY' , 'Michigan' : 'MI'}

#create a basic sets of states and some cities in them
cities = {'CA': 'San Francisco', 'MI' : 'Detroit' , 'FL' : 'Jacksonville'}

# add some more cities 
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY state has : ", cities['NY'])
print("OR state has : ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbrevation is : ", states['Michigan'])
print("Florida's abbrevation is : ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has : ", cities[states['Michigan']])

#print every state abbreviation
print('-' * 10)
for state , abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")


