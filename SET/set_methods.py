# #SET

# #ADD ELEMENT IN SET LIST
s={1,2,3,4}
s.add(5)
print(s)

# #ADDING MORE THAN ONE ELEMENTS IN SET LIST
s.update({6,7})
print(s)

#DELETE ELEMENTS IN THE SET LIST
s={1,2,5,8,9}
s.pop(2)
print(s)

s.clear()
print(s)

# #DELETE ELEMENTS IN THE SET LIST 
s={5,6,7,9,8,0}
s.remove(8)#we can see the error in remove
print(s)

s={3,6,7,8}
s.discard(5)#we can't see any error in discard
print(s)




