# import re
# s='welcome'
# res=re.search('w',s)
# print(res)

# import re
# s='welcome'
# res=re.search('w.',s)#[---Is there any character after the given character---]
# print(res)


# import re
# s='welcome'
# res=re.search('w.*',s)#  [--- Is there 0 or any character after the given character, it works only one character ---]
# print(res)


# import re
# s='we l come'#[--- spacing also include ---]
# res=re.search('w.+',s)#  [---- Is there 1 or any character after the given character ----]
# print(res)

# import re
# s='we l come'
# res=re.search('w.?',s)#  [---- Is there 0 or 1 any  character after the given character ----]
# print(res)

# import re
# s='Welcome'
# res=re.search('[a-z]',s)#[---- is there small letter in character , print first small letter ----]
# print(res)


# import re
# s='Welcome'
# res=re.search('[A-Z]',s)#[---- is there capital letter in character , print first captical letter ----]
# print(res)


# import re
# s='We1co3e'
# res=re.search('[0-9]',s)#[---- is there numbers 0-9 letter in character ----]
# print(res)

# import re
# s='Welcome'
# res=re.search('[A-Za-z0-9]',s)#[---- Is there any one ca[ital,small,number occured in s ----]
# print(res)

# import re
# s='Wa3'
# res=re.search('[A-Z][a-z][0-9]',s)#[---- Is there any one capital,small,number occured in s ----]
# print(res)


import re
s='Welcome@123'
res=re.search('[A-Z].{11}',s)#[---- Is there any one ca[ital,small,number occured in s ----]
print(res)

