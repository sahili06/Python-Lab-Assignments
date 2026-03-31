class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        b = Book(title, author)
        self.books.append(b)
        print("Book added successfully")

    def lend_book(self):
        title = input("Enter book title to lend: ")
        for b in self.books:
            if b.title == title and b.available:
                name = input("Enter member name: ")
                m = Member(name)
                b.available = False
                print("Book issued to", m.name)
                return
        print("Book not available")

    def return_book(self):
        title = input("Enter book title to return: ")
        for b in self.books:
            if b.title == title:
                b.available = True
                print("Book returned successfully")
                return
        print("Book not found")

    def display_books(self):
        if len(self.books) == 0:
            print("No books in library")
        else:
            for b in self.books:
                status = "Available" if b.available else "Issued"
                print("Title:", b.title, "| Author:", b.author, "| Status:", status)


lib = Library()

while True:
    print("\n1. Add Book")
    print("2. Lend Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        lib.add_book()
    elif ch == 2:
        lib.lend_book()
    elif ch == 3:
        lib.return_book()
    elif ch == 4:
        lib.display_books()
    elif ch == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")
