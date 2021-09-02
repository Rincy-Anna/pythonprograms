#5. What is method overriding give an example using Books class?

class Book:
    def print(self,book_name):
        self.book_name=book_name
        print("Book_name: ",self.book_name)
class Author(Book):
    def print(self,author):
        self.author=author
        print("Author_name: ",self.author)
au=Author()
au.print("Vaikkam Muhammed Basheer")
