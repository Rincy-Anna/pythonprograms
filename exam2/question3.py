#3. Create a Book class with instance Library_name, book_name, author, pages?

class Book:
    def setval(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def print(self):
        print("Library name: ",self.library_name)
        print("Book name: ",self.book_name)
        print("Author: ",self.author)
        print("Pages: ",self.pages)

bo=Book()
bo.setval("Avanty Publications","Robinson Crusoe","Daniel Defoe",108)
bo.print()
