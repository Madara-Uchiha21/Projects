# Using regex function

'''
1. Here we need alphabate in small case
2. Number from 0-9 shall be there
3. . _ shall be 1-1 at a time
4. @ shall be one
5. "." at 2 or 3 from last 
'''

import re

Email_condition = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"     

#? in regex is used to provide one thing at one from ._, if more thaen one it will return false
# @ is special character and \w is used to search that special character from string
# {} are defining particular conditions , and {2,3} - 2,3 shows that how many time anything have to searched
# $ is if we are searching from backword

User_Email = input("Enter your Email: ")

if re.search(Email_condition,User_Email):
    print("Right Email")
else:
    print("Wrong Email")

