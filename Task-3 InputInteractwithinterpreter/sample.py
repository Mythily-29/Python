import sys
import random

users_list=['delisha a k','bhavanaak','hemaak','shashwanthak','jennie kim','doreme','suzuka','chutki','yumiko','nobita','chikku','banty']

sys.argv=[sys.argv[0],random.choice(users_list)]


full_name=sys.argv[1]
email=full_name.replace(' ','.')+'@gmail.com'


if(full_name and email):
    print('Name is :',full_name)
    print('Your email is generated:',email)
    print('Executed successfully')
else:
    print('Failed to get the details')
