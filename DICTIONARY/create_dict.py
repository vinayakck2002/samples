#update the key value 
l=["name","age","place"]
d=dict.fromkeys(l,"null")
print(d)
d.update({"name":"abhi"})
print(d)
d.update({"age":21})
print(d)
d.update({"place":"calicut"})
print(d)

#---------------------------------------------------