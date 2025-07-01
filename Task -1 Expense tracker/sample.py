expenses=[]

while True:

    print('1: Add expense  2: show expense  3.exit')

    user=int(input('Enter a number:'))

    if user==1:
        item=input('Enter item:')
        amount=int(input('Enter amount:'))
        if(item and amount):
            expenses.append({'item':item,'amount':amount})
            print('Your expenses:',expenses)


    elif user==2:
        finalexpense=0
        for i in expenses:
            finalexpense += i['amount']
        print('Your expense amount:',finalexpense)

    elif user==3:
        print('You exitted')
        break



