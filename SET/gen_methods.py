#SET

s={1,2,3,7}
s1={1,2,3,4,5,6}
print(s1.difference(s))
print(s1.intersection(s))
print(s1.isdisjoint(s))
print(s1.issubset(s))
print(s1.issuperset(s))
print(s1.symmetric_difference(s))


s2=s1.copy()

s.difference_update(s1)
print(s)

s.intersection_update(s1)
print(s)

s.symmetric_difference_update(s1)
print(s)
