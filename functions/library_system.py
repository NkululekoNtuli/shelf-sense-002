DATABASE_FILE = "./database/books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        if db == False:
            db = DATABASE_FILE

def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    # TODO: Append the book's title and author to the database file
    with open(DATABASE_FILE, 'a') as db:
        db.write(f"\nTitle,Author \n{title},{author}")

# add_book("The end", "nkulu" )



def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # TODO: Implement logic to search for a book in the database file
    with open(DATABASE_FILE, 'r') as db:
        file = db.readlines()

    for i in range(len(file)):
        file_split = file[i].split(",")
        if title == file_split[0]:
            return file[i]
        elif i == 3:
            return None
# print(search_book("The end"))


def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries
