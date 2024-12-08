# Question:
# Design a Library class that manages books and their availability. The system should include the following:

# Classes:

# Book:

# Attributes:
# title (string): Title of the book.
# author (string): Author of the book.
# copies_available (int): Number of copies available.
# Methods:
# add_copies(number): Adds copies to the book.
# borrow_book(): Decreases available copies if there are copies; otherwise, print "Not available."
# return_book(): Increases available copies.
# Library:

# Attributes:
# books (list): A list of Book objects.
# Methods:
# add_book(book): Adds a new Book object to the library.
# search_book(title): Searches for a book by title and returns it.
# borrow_book(title): Allows a user to borrow a book if it's available.
# return_book(title): Allows a user to return a borrowed book.
# list_books(): Lists all books in the library with their availability.
# Tasks:

# Add three books to the library:
# "1984" by George Orwell (5 copies)
# "To Kill a Mockingbird" by Harper Lee (3 copies)
# "The Great Gatsby" by F. Scott Fitzgerald (4 copies)
# Borrow "1984" and "The Great Gatsby."
# Return "1984."
# Print all books in the library with their current availability.

class Book: #class
    def __init__(self,title,author,copies_available):#constructor
        self.title=title
        self.author=author
        self.copies_available=copies_available
    def add_copies(self,number):#method
        self.copies_available+=number   
    def Borrow_book(self):#method
        if self.copies_available>0: #condition    
            print(self.copies_available,"Is available")
        else:
            print("Not available")
    def Return_book(self):#method
        self.copies_available+=1
        print("Incraese available copies")

class Library: #class
    def __init__(self,Book):#constructor
        self.Book=Book    
    def Add_Book(self,Book):#method
        self.Book.append(Book)
        print("Book Added")
        
    def Search_Book(self,title):#method
        for i in self.Book:
            if i.title==title:
                return i
        return None 
    def Borrow_book(self,title):#method
        book=self.Search_Book(title)
        if book:
            book.Borrow_book()
        else:
            print("Book not found") 
    def Return_book(self,title):#method
        book=self.Search_Book(title)    
        if book:
            book.Return_book()
        else:
            print("Book not found") 
    def List_Books(self):#method
        for i in self.Book:
            print(i.title,i.copies_available)

book1=Book("1984","George Orwell",5)
book2=Book("To Kill a Mockingbird","Harper Lee",3)
book3=Book("The Great Gatsby","F. Scott Fitzgerald",4)
l=Library([book1,book2,book3])
l.Add_Book(book1)
l.Borrow_book("1984")
l.Return_book("1984")
l.List_Books()      
