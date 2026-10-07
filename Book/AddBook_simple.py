import requests
import json

from DataFileInitialisation import BookDataHashmapinitialise

class AddBookData:
    def __init__(self,bookname,bookcode,isbn,author,publisher,bookcopies,language,publishedDate,categories,averageRating,pageCount,description):
        self.bookname = bookname
        self.bookcode = bookcode
        self.isbn = isbn
        self.author = author
        self.publisher = publisher
        self.publishedDate = publishedDate
        self.language = language
        self.categories = categories
        self.averageRating = averageRating
        self.bookcopies = bookcopies
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

    @classmethod
    def get(cls, acqusitionmethod, isbn, bookcopies):
        found = False
        while not found:
            headers = {"User-Agent": "BookInfo (s221103@sttss.edu.hk)"} #enter the sch staff email
            apikey  = "AIzaSyDVvbCUM8MBZjQNns-7oHeAQFhAXQW2uZE"
            url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={apikey}"
            try:
                response = requests.get(url, headers=headers, timeout= 10)
                data = response.json()
                if "items" in data:
                    book_info = data["items"][0]["volumeInfo"]
                    bookname = book_info.get("title")
                    bookcodelanguage_temp = book_info.get("language")
                    if bookcodelanguage_temp[0:2] == "en":
                        bookcodelanguage_temp = "e"
                    elif bookcodelanguage_temp[0:2] == "zn":
                        bookcodelanguage_temp = "c"
                    else:
                        bookcodelanguage_temp = "o"
                    bookcode = f"{bookcodelanguage_temp}-{acqusitionmethod}-{isbn}-{bookcopies}"
                    isbn = isbn
                    author = book_info.get("authors")
                    publisher = book_info.get("publisher")
                    publishedDate = book_info.get("publishedDate")
                    language = book_info.get("language")
                    pageCount = book_info.get("pageCount")
                    if pageCount == 0:
                        pageCount = "N/A"
                    categories = book_info.get("categories")
                    averageRating = book_info.get("averageRating")
                    if averageRating == None:
                        averageRating = "N/A"
                    description = book_info.get("description")
                    if description == None:
                        description = "N/A"
                    found = True
                elif "error" in data:
                    apikey = (input("Invalid api key, please re-enter it")).strip()
                else:
                    found = True
                    bookname,bookcode,author,publisher,bookcopies,language,publishedDate,categories,averageRating,pageCount,description = None ,None, None, None, None, None, None, None, None, None, None
                    isbn = isbn
            except requests.exceptions.RequestException as error:
                print("Network Error, please try again")
            except requests.exceptions.ConnectionError as error:
                print("Connection Error, please ret again")
        return cls(bookname,bookcode,isbn,author,publisher,bookcopies,language,publishedDate,categories,averageRating,pageCount,description)

        
def AddBook():
    with open("data/BookInfo.json") as bookinfofile:
        data = json.load(bookinfofile)
    bookinfo = BookDataHashmapinitialise(data)

    with open("data/BookStatus.json") as bookstatusfile:
        data = json.load(bookstatusfile)
    bookstatus = BookDataHashmapinitialise(data)

    books = []
    
    print("type the isbn code of books in the followings.")
    print("type N/A when all the books are inputted")
    k = 0
    #isbn = str.strip(input(f"{k}. ")).replace("-", "")
    #if isbn != "N/A":
    #    check = False
    #    while not check:
    #        acqusitionmethod = str.strip(input("acqusition method. bought/donated"))
    #        if acqusitionmethod == "bought" or acqusitionmethod == "Bought":
    #            acqusitionmethod = "b"
    #            check = True
    #        elif acqusitionmethod == "donated" or acqusitionmethod == "Donated":
    #            acqusitionmethod = "d"
    #            check = True
    #        else:
    #            print("invalid input for acqusitionmethod")
    #bookcopies = str.strip(input("book copy number"))
    #book_temp = AddBookData.get(acqusitionmethod, isbn, bookcopies)
    #books += [book_temp]
    finish = False
    while not finish:
        k += 1
        isbn = str.strip(input(f"{k}. ")).replace("-", "")
        if isbn != "N/A":
            check = False
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
            book_temp = AddBookData.get(acqusitionmethod, isbn, bookcopies)
            books += [book_temp]
        if isbn == "N/A":
            finish = True


    print("The following books are the book that will be added.")
    print("please double check to make sure that all the book info is correct.")
    print("if any of the followings information is wrong, please type the number below")
    for i in range(len(books)):
        if books[i].bookcode == None:
            print(f"{i+1}. isbn:{books[i].isbn} book not found")
        else:
            print(f"{i+1}. bookname:{books[i].bookname}, bookcode:{books[i].bookcode}, isbn code:{books[i].isbn}, author:{books[i].author}, publisher:{books[i].publisher}")
    choice = 0
    while choice != "3":
        print(
            "1. check on some of the book information in detail\n"
            "2. correct wrong book information\n"
            "3. all the book data is correct and can be stored"
        )
        choice = input("please input your option by typing the number")
        match choice:
            case n if n == "1":
                    checkindex = int(input("please input the index of the book that you can to check(one at a time)"))
                    print(
                        f"""
book name: {books[checkindex-1].bookname}
isbn code: {books[checkindex-1].isbn}
book code: {books[checkindex-1].bookcode}
author: {books[checkindex-1].author}
publisher: {books[checkindex-1].publisher}
book copies: {books[checkindex-1].bookcopies}
book language: {books[checkindex-1].language}
published date: {books[checkindex-1].publishedDate}
categories: {books[checkindex-1].categories}
average rating: {books[checkindex-1].averageRating}
page count: {books[checkindex-1].pageCount}
desciption: {books[checkindex-1].description}
"""
                    )
            case n if n == "2":
                checkindex = int(input("please input the index of the book that you can to check(one at a time)"))
                print("type N/A if there is no need to change the data")
                tempbookinfo = {}
                tempbookinfo["bookname"] = input(f"book name: {books[checkindex-1].bookname}")
                tempbookinfo["isbn"] = input(f"isbn code: {books[checkindex-1].isbn}")
                tempbookinfo["bookcode"] = input(f"book code: {books[checkindex-1].bookcode}")
                tempbookinfo["author"] = input(f"author: {books[checkindex-1].author}")
                tempbookinfo["publisher"] = input(f"publisher: {books[checkindex-1].publisher}")
                tempbookinfo["bookcopies"] = input(f"book copies: {books[checkindex-1].bookcopies}")
                tempbookinfo["language"] = input(f"book language: {books[checkindex-1].language}")
                tempbookinfo["publishedDate"] = input(f"published date: {books[checkindex-1].publishedDate}")
                tempbookinfo["categories"] = input(f"categories: {books[checkindex-1].categories}")
                tempbookinfo["averageRating"] = input(f"average rating: {books[checkindex-1].averageRating}")
                tempbookinfo["pageCount"] = input(f"page count: {books[checkindex-1].pageCount}")
                tempbookinfo["description"] = input(f"desciption: {books[checkindex-1].description}")
                for i, j in vars(books[checkindex-1]).items():
                    if tempbookinfo[i] != "N/A":
                        setattr(books[checkindex-1], f"{i}", tempbookinfo[i])
    for i in books:
        if i.bookname != None and i.bookname != "":
            bookinfo[i.isbn] = {
            "bookcode": i.bookcode,
            "bookname":i.bookname,
            "isbn":i.isbn,
            "author":i.author,
            "publisher":i.publisher,
            "bookcopies":i.bookcopies,
            "language":i.language,
            "publishedDate":i.publishedDate,
            "categories":i.categories,
            "averageRating":i.averageRating,
            "pageCount":i.pageCount,
            "description":i.description
            }
            bookstatus[i.isbn] = {"status": "a", "duedata": None}
    with open("data/BookInfo.json","w") as BookInfoData:
       json.dump(bookinfo.hashmap, BookInfoData, indent=3)
    with open("data/BookStatus.json", "w") as BookStatusFile:
        json.dump(bookstatus.hashmap, BookStatusFile, indent=3)