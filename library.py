print("Welcome to library management system")
# books_list = ["Book1", "Book2", "Book3"]
books_list = [
  {
    "name": "Book1",
    "available": True
  },
  {
    "name": "Book2",
    "available": True
  },
  {
    "name": "Book3",
    "available": False
  }
]

option = int(input("Enter: "))
if (option == 1):
  print("View all books.")
  for i in range(0, len(books_list)):
    print(books_list[i])
elif (option == 2):
  # you have to correct this function
  print("add book to the list.")
  book = input("Enter the name of the book: ")
  new_book = {
    "name": book,
    "available": False
  }
  books_list.append(new_book)
  print(books_list)
  print("your book is added to the original library.")
elif (option == 3):
  print("borrow a book")
  name = input("Enter the name of the book you want to borrow: ")

  for i in range(0, len(books_list)):
    if (books_list[i]["name"] == name):
      print("we have this book. checking its availability. ")
      if (books_list[i]["available"] == True):
        print("The book is available. you can boorow this book.")
        books_list[i]["available"] = False
        print(books_list)
        break
      else:
        print("Sorry this book ain't ava  ilable. Come back later.")

elif (option == 4):
  print("return a book")

    
    
    
      
    
#     Bonus Challenges:
# Add a user authentication system (admin vs. normal users).
# Store book data in a file (books.json or books.txt) to persist data.
# Implement a search function to find books by title or author.