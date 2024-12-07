class Book:
    def __init__(self,title,author,copies_available):
        self.title=title
        self.author=author
        self.copies_available=copies_available

    def Add_copies(self,number):
        self.copies_available+=number
        print("Adds copies to the book")
    def Borrow_book(self):
        if self.copies_available>0:
            print(self.copies_available,"Is available")
        else:
            print("Not available")
    def Return_book(self):
        self.copies_available+=1
        print("Incraese available copies")

class Library:
    def __init__(self,Book):
        self.Book=[]
        
    def Add_Book(self,Book):
        self.Book.append(Book)
        print("Book Added")




        

