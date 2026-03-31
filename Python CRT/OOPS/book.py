'''
write a py prog to create a book class declare the styates as BookName, AuthorName, PublisherName,PublishedDate, CategoryOfBook
1)vreate 5 objects and intialize using  constructor where out of 5 
     create 1st object using one parameterized constructor
     create 2st object using two parameterized constructor
     create 3rd object using zero parameterized constructor
     create 4th object using four parameterized constructor
     create 5th object using five parameterized constructor
2) Access the values using Accessor Methods
3) update the values using Mutator method for name of the book
 

'''
class Book:
    def __init__(self, BookName=None, AuthorName=None, PublisherName=None, PublishedDate=None, CategoryOfBook=None):
        self.BookName = BookName
        self.AuthorName = AuthorName
        self.PublisherName = PublisherName
        self.PublishedDate = PublishedDate
        self.CategoryOfBook = CategoryOfBook

    def set_details(self, BookName, AuthorName, PublisherName, PublishedDate, CategoryOfBook):
        self.BookName = BookName
        self.AuthorName = AuthorName
        self.PublisherName = PublisherName
        self.PublishedDate = PublishedDate
        self.CategoryOfBook = CategoryOfBook

    def get_details(self):
        print(f"Book Name: {self.BookName}")
        print(f"Author Name: {self.AuthorName}")
        print(f"Publisher Name: {self.PublisherName}")
        print(f"Published Date: {self.PublishedDate}")
        print(f"Category of Book: {self.CategoryOfBook}")
    def update_book_name(self, new_name):
        self.BookName = new_name
b1 = Book("Wings of fire")
b2 = Book("YOGA", "jYOTHI")
b3 = Book()
b4 = Book("RAMAYAN", "Valmiki", "Gita press", "1950")
b5 = Book("Mahabharat", "Vyas", "Geeta", "1800", "mythology")
b1.get_details()
b2.get_details()
b3.get_details()
b4.get_details()
b5.get_details()
print("\n--- Updating Book Name for book2 ---")
b2.update_book_name("The Pilgrimage")
b2.get_details()