


import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email=input()
try:
    (re.fullmatch(regex, email))
    print('yes')
except:
    print('no')