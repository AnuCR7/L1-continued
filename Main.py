fruit={
    'apple':'red',
    'pineapple':'yellow',
    'banana':'yellow',
    'strawberry':'red'

}
print(fruit)
#looping through the dictionary
for i in fruit:
    print(i)
#accessing items
print(fruit['apple'])

#get all keys
print(fruit.keys())

#get all values
print(fruit.values())

#get all key value pairs#
print(fruit.items())

#checking if key exists
if 'apple' in fruit:
    print('apple is in the dictionary')

#changing a value in a dictionary
fruit['pineapple']= 'orange'
print(fruit)

#adding a key value pair
fruit['tangerine']='orange'
print(fruit)

#deleting a key value pair
del fruit['pineapple']
print(fruit)




















