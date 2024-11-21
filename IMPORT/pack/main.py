# import module1
# module1.sample()#calling function
# print(module1.l)#calling the list 

#-------------------------------------------------------------#

# import module1 as m #rename the module name
# m.sample()
# print(m.l)

#--------------------------------------------------------------#

# from module1 import sample,l#from module_name import function_name,variable
# sample()
# print(l)# L variable declared in top

#-------------------------------------------------------------#

from module1 import * #from module_name import * (Calling all fucntion and variables use *)
sample()
print(l)


