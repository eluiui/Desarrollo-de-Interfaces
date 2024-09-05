class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        
class Book():
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price    
    
    def printBook(self):
        print("Author:", self.author.name)
        print("Title:", self.title)
        print("Price:", self.price)
    
def main():
    stephen_king = Author("Stephen King", "American")
    it_book = Book(stephen_king, "It", 10.99)
    
    it_book.printBook()
    
if __name__ == "__main__":
    main()