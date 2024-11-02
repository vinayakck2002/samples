l=["name","author","year"]
while True:
    
    print("1.Add Book\n2.update Book\n3.Remove Book\n4.View All Book\n5.Search Book\n6.Exit")
    choice=int(input("Enter your choice :"))
        
    if(choice==1):
        code=int((input("Enter a code :")))
        name=input("Enter the Title :")
        author=(input("Enter the author name :"))
        year=int(input("Enter the year of book :"))
        l.append({"name":name, "author":author,"year":year})
        print(l,"added successfully")
            
      
        
        
    elif(choice==4):
        print(l)
    elif(choice==6):
        break
    else:
        print("Invalid")        
        
        
        
        
        
        
    
        
       
        
        
    
    
        
        
            
        

