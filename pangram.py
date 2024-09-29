number=input('Enter any number:')
numbers={
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0,
    '0':0
}

for i in number:
    if i in numbers:
        numbers[i]+= 1

pangram=True
for i in numbers.values():
    if i==0:
        pangram=False
if pangram:
    print('This is a pangram')
else:
    print('This is not a pangram')


































