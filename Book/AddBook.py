'''
require user to input:
book name
author
brought or donated
chinese or english or others

book code [L6][L5]-[isbn]-[book copies]

'''
import requests
import csv
import threading

from Book.Booksearch import BookDataHashmap

class AddBookData:
    def __init__(self,bookname,bookcode,author,isbn,publisher,publishedDate,language,pageCount,categories,averageRating,description):
        self.bookname = bookname
        self.bookcode = bookcode
        self.isbn = isbn
        self.author = author
        self.publisher = publisher
        self.publishedDate = publishedDate
        self.language = language
        self.categories = categories
        self.averageRating = averageRating
        self.pageCount = pageCount
        self.description = description

    def __str__(self):
        return(f"""
bookname : {self.bookname}
bookcode : {self.bookcode}
author : {self.author}
publisher : {self.publisher}
publishedDate : {self.publishedDate}
language : {self.language}
pageCount : {self.pageCount}
categories : {self.categories}
averageRating : {self.averageRating}
description : {self.description}
            """)

    def __eq__(self, other):
        if isinstance(other, self):
            return (self.isbn == other.isbn)
        return False
    @classmethod
    def get(cls, acqusitionmethod, isbn, bookcopies):
        found = False
        while not found:
            headers = {"User-Agent": "BookInfo (s221103@sttss.edu.hk)"} #enter the sch staff email
            apikey  = "AIzaSyDVvbCUM8MBZjQNns-7oHeAQFhAXQW2uZE"
            openlibraryurl = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
            url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={apikey}"
            try:
                response = requests.get(url, timeout=10)
                data = response.json()
                if "items" in data:
                    book_info = data["items"][0]["volumeInfo"]
                    bookname = book_info.get("title")
                    bookcode = f"{book_info.get("language")}-{acqusitionmethod}-{isbn}-{bookcopies}"
                    isbn = isbn
                    author = book_info.get("authors")
                    publisher = book_info.get("publisher")
                    publishedDate = book_info.get("publishedDate")
                    language = book_info.get("language")
                    pageCount = book_info.get("pageCount")
                    categories = book_info.get("categories")
                    averageRating = book_info.get("averageRating")
                    description = book_info.get("description")
                    found = True
                elif "error" in data:
                    apikey = (input("Invalid api key, please re-enter it")).strip()
                else:
                    found = True
                    bookname,bookcode,isbn,author,publisher,bookcopies,language,publishedDate,categories,averageRating,pageCount,description = None
            except requests.exceptions.RequestException as error:
                print("Network Error, please try again")
            except requests.exceptions.ConnectionError as error:
                print("Connection Error, please ret again")
        return cls(bookname,bookcode,isbn,author,publisher,bookcopies,language,publishedDate,categories,averageRating,pageCount,description)

class AddBookStatus:
    def __init___(self):
        self.status = 0
        self.duedate = None


def CreateBook():
    BookDataFile = BookDataHashmap()
    BookStatusFile = BookDataHashmap()
    print("type the isbn code of books in the followings.")
    print("type N/A when all the books are inputted")
    i = 1
    bookdt = []
    def AddBook():
        print("type the isbn code of books in the followings.")
        print("type N/A when all the books are inputted")
        i = 1
        AddBookUI()

    def AddBookUI():
        global i, BookDataFile
        isbn = str.strip(input(f"{i}. ")).replace("-", "")
        if isbn != "N/A":
            while not check:
                acqusitionmethod = str.strip(input("acqusition method. bought/donated"))
                if acqusitionmethod == "bought" or acqusitionmethod == "Bought":
                    acqusitionmethod = "b"
                    check = True
                elif acqusitionmethod == "donated" or acqusitionmethod == "Donated":
                    acqusitionmethod = "d"
                    check = True
                else:
                    print("invalid input for acqusitionmethod")
            bookcopies = str.strip(input("book copy number"))
            _AddBookUI = threading.Thread(target=AddBookUI)
            _AddBookData =threading.Thread(AddBookData.get, args=(acqusitionmethod, isbn, bookcopies))
            bookdt += [_AddBookData.start()]
            i += 1
            _AddBookUI.start()

    newbookstatus = AddBookStatus()
    #for i in bookdt:
        #BookDataFile.__setitem__(i.bookcode, i)
        #BookStatusFile.__setitem__(i.bookcode,newbookstatus)
    with open("BookInfo.csv","a") as BookInfoData:
        BookDataFieldnames = ["bookcode","bookname","isbn","author","publisher","bookcopies","language","publishedDate","categories","averageRating","pageCount","description"]
        BookStatusFieldnames = ["bookcode", "status", "duedate"]
        writer = csv.DictWriter(BookDataFile, fieldnames=BookDataFieldnames)
        for i in range(len(bookdt)):
            writer.writerow({
                "bookcode": bookdt[i].bookcode,
                "bookname":bookdt[i].bookname,
                "isbn":bookdt[i].isbn,
                "author":bookdt[i].author,
                "publisher":bookdt[i].publisher,
                "bookcopies":bookdt[i].bookcopies,
                "language":bookdt[i].language,
                "publishedDate":bookdt[i].publishedDate,
                "categories":bookdt[i].categories,
                "averageRating":bookdt[i].averageRating,
                "pageCount":bookdt[i].pageCount,
                "description":bookdt[i].description
                })
    with open("BookStatus.csv","a") as BookStatusFile:
        writer = csv.DictWriter(BookDataFile, fieldnames=BookStatusFieldnames)
        for i in range():
            writer.writerow({
                "status": "0",
                "duedate": None
                })