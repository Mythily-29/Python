import random

list='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyz!@#$&).?/1234567890'

user=int(input('Enter password pattern:'))
length=int(input('Enter password length:'))
password=''

if(length >=8):
    for i in range(user):
        for j in range(length):
            password +=random.choice(list)
            if(len(password)==length):
                print('Your password are:',password)
                password=''
else:
    print('Enter password length greater than 8')
    

    

