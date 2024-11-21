l=['apple','orange','kiwi','banana']
letter=input("Enter a value")
#filter(function,iterable)
#print(list(filter(lambda a:Letter in a,l)))
data=filter(lambda a:letter in a,l)
print(list(data))

    