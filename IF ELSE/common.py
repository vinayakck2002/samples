
python={"akshay",'vinayak','abhinav'}
java={"akshay","rahul","raayan"}
php={"raayan","sreerag","akshay"}

print("1.Common in python and java\n2.Common in java and php\n3.Common in all batches\n4.Uncommon in all batches")

check=int(input("Enter your choice:"))

if(check==1):
    print(java.intersection(python))
    
elif(check==2):
    print(java.intersection(php))
    
elif(check==3):
    print(python.intersection(java,php))
    
elif(check==4):
   union= python.union(java,php)  
   inter1 = python.intersection(java)  
   inter2 = java.intersection(php)  
   s = union - inter1 - inter2 
   print(s)
else:
    print("invalid")

