class Library:
    
    def __init__(self, book):
        self.book=[]
        
        
    def add_book(self, book):
        self.book.append(book)
    

   



class Book:
    
    def __init__(self, title, author, isbn , available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        
     
        
    def display_info(self):
        if self.available ==False:
            print("Not avalable")
        else:
            print(self.available)
            
        print(self.title)
        print(self.author)
        print(self.isbn)
 
     
 
    
 
    
class Member:
    
    
    def __init__(self, name, membership_id ):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []
      
        
    def borrow_book(self,book):
        if book in self.borrow_book:
            self.borrow_book.remov(book)
            if self.borrow_book == False:
        
               print(self.name +" has borrowed " + self.title)
            else:
                print("The book is currently not available")
        
    def return_book(self, book):
         
         if book in self.borrow_book:
             self.borrow_book.append(book)
             if self.borrow_book == True:
                 print(self.name +" has returned " + self.title)
             else:
                 print( "The book did not borrow")
                 
             
          
    
                
             
        
class StaffMember(Member):
    
    def __init__(self,staff_id):
        self.staff_id = staff_id
        
    
    def add_book(self, title, author, isbn):
        
        new_book = Book
        Library.add_book(new_book)
        print(Book.title + "has been added")
        
        
one=membership_id("membership_id") 
print(one.get_membership_id())      
one.set_membership_id(123456)
one=isbn("isbn")
print(one.get_isbn())       
one.set_isbn(444)        
        