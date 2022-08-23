class library():
    def __init__(self):
        self.bookname = input("Book name ")
        self.ISBN = int(input("ISBN "))
        self.author = input("Author ")

    def display(self):
        print(self.bookname, self.ISBN, self.author)

    def create(self):
        self.new = library()

book = library()
book.display()
