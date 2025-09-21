from book import Book # Import Book class from book.py

def add_book(library):
  """Add new book to library by prompting user for information."""
  title = input("Enter book title: ")
  author = input("Enter book author: ")
  isbn = input("Enter book ISBN: ")
  new_book = Book(title, author, isbn) # Create new book instance
  library.append(new_book) # Add book to library list
  print(f"'{title}' by '{author}' has been added to your library. \n") 

def list_books(library):
  """Print all books in library or print message if empty."""
  if not library:
    print("No books in library. :( \n")
    return
  print("Books in library: ")
  for book in library:
    print(book)
  print()
  
def find_books(library, query):
  """
  Search for books in library by title or author.

  Args:
    library (list): List of book objects
    query (str): Search term to look for.
  Returns:
    list: A list of matching book objects.
  """
  query = query.lower()
  return [book for book in library if query in book.title.lower() or query in book.author.lower()]
    
def main():
  """Run display menu loop for the library manager program."""
  
  my_library = []
  
  while True:
    # Display menu options
    print("Library Manager Menu:")
    print("1. Add a new book.")
    print("2. List all books.")
    print("3. Find a book.")
    print("4. Exit the program. \n")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
      add_book(my_library)
    elif choice == "2":
      list_books(my_library)
    elif choice == "3":
      query = input("Enter book title or author to find a book: ")
      search_result = find_books(my_library, query)
      if search_result:
        print("Books found:")
        for book in search_result:
          print(book)
      else:
        print("No books found. :(")
    elif choice == "4":
      print("Exiting library manager. See you again soon! :)")
      break
    else:
      print("Invalid response. Please enter a number between 1 and 4. \n")
    
if __name__ == "__main__":
  main()
