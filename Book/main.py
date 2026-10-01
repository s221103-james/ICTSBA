from ReadBook import ReadBook
from AddBook_simple import AddBook
from AmendBook import AmendBook
from DeleteBook_simple import DeleteBook

def main():
    print("1. Search Book")
    print("2. Add Book")
    print("3. Amend Book")
    print("4. Delete Book")
    choice = str(input("input your choice by typing the index"))
    match choice:
        case "1":
            ReadBook()
            print(132456)
        case "2":
            AddBook()
        case "3":
            AmendBook()
        case "4":
            DeleteBook()
        case _ :
            print("invalid index")

main()