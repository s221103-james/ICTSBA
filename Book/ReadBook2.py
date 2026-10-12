import json
import math

from DataFileInitialisation import BookDataHashmapinitialise

class BookData:
    def __init__(self,bookname,bookcode,isbn,author,publisher,bookcopies,language,publishedDate,categories,averageRating,pageCount):
        self.targetcondition = {}
        self.bookcode = bookcode
        self.isbn = isbn
        if self.isbn == "N/A" and self.bookcode != "N/A":
            self.isbn = self.bookcode[4:-2]
        if bookname != "N/A":
            self.targetcondition["bookname"] = bookname
        if author[0] != "N/A":
            self.targetcondition["author"] = author
        if publisher != "N/A":
            self.targetcondition["publisher"] = publisher
        if publishedDate != "N/A":
            self.targetcondition["publishedDate"] = publishedDate
        if language != "N/A":
            self.targetcondition["language"] = language
        if categories[0] != "N/A":
            self.targetcondition["categories"] = categories
        if averageRating != "N/A":
            self.targetcondition["averageRating"] = averageRating
        if bookcopies != "N/A":
            self.targetcondition["bookcopies"] = bookcopies
        if pageCount != "N/A":
            self.targetcondition["pageCount"] = pageCount
        self.targetfound = []
        self.subtargetfound = []
        self.authorfound = []
    @classmethod
    def get(cls):
        bookname = input("bookname: ")

        bookcode = input("bookcode: ")

        isbn = input("isbn: ")

        check = False
        while not check:
            acqusitionmethod = str.strip(input("acqusition method. bought/donated"))
            if acqusitionmethod == "bought" or acqusitionmethod == "Bought":
                acqusitionmethod = "b"
                check = True
            elif acqusitionmethod == "donated" or acqusitionmethod == "Donated":
                acqusitionmethod = "d"
                check = True
            elif acqusitionmethod == "N/A":
                check = True
            else:
                print("invalid input for acqusitionmethod")

        author = input("author(split authors by using ,): ").split(",")

        publisher = input("publisher: ")

        publishedDate = input("published date: ")

        language = input("language: ")

        if language == "english" or language == "English":
            bookcodelanguage_temp = "e"
        elif language == "chinese" or language == "Chinese":
            bookcodelanguage_temp = "c"
        else:
                bookcodelanguage_temp = "o"

        categories = input("catergories(split terms by using ,): ").split(",")

        averageRating = input("average rating: ")

        bookcopies = input("book copies: ")

        pageCount = input("page count: ")

        if bookcode != "N/A" and isbn != "N/A" and bookcopies != "N/A" and acqusitionmethod != "N/A" and language != "N/A":
            bookcode = f"{bookcodelanguage_temp}-{acqusitionmethod}-{isbn}-{bookcopies}"

        return cls(bookname,bookcode,isbn,author,publisher,bookcopies,language,publishedDate,categories,averageRating,pageCount)

def OutputUI(z):
    print(f"bookname: {z['bookname']}")
    print(f"isbn: {z['isbn']}")
    print(f"book code: {z['bookcode']}")
    print(f"author: {z['author']}")
    print(f"publisher: {z['publisher']}")
    print(f"bookcopies: {z['bookcopies']}")
    print(f"language; {z['language']}")
    print(f"publisheddate: {z['publishedDate']}")
    print(f"categories: {z['categories']}")
    print(f"averageRating: {z['averageRating']}")
    print(f"pagecount: {z['pageCount']}")
    print(f"description: {z['description']}")
    print(f"book available: {z['status']}")

def ReadBook2():
    with open("data/BookInfo.json") as bookinfofile:
            data = json.load(bookinfofile)
    bookinfo = BookDataHashmapinitialise(data)
    with open("data/BookStatus.json") as bookstatusfile:
        data = json.load(bookstatusfile)
    bookstatus = BookDataHashmapinitialise(data)

    target = BookData.get()
    check = 0
    checkauthor = None
    for i in target.targetcondition:
        check += len(target.targetcondition[i])
        if i == "author":
            checkauthor = len(target.targetcondition["author"])
            target.authorfound = [[]*checkauthor]

    if target.bookcode != "N/A":
        for i in range(len(bookinfo[target.isbn])):
            if bookinfo[target.isbn][i][1]["bookcode"] == target.bookcode:
                target.targetfound += [bookinfo[target.isbn][i][1]]
            if bookinfo[target.isbn][i][0] == target.isbn:
                target.subtargetfound += [bookinfo[target.isbn][i][1]]

    elif target.isbn != "N/A":
        for i in range(len(bookinfo[target.isbn])):
                if bookinfo[target.isbn][i][0] == target.isbn:
                    target.targetfound += [bookinfo[target.isbn][i][j]]


    else:
        for i in range(len(bookinfo.hashmap)): #each hashcode
            for j in range(len(bookinfo.hashmap[i])): #same hashcode
                #check no. if print or not
                if len(target.targetfound) %10 == 0 and len(target.targetfound) >= 20:
                    for z in range(len(target.targetfound)-20, len(target.targetfound)-9):
                        print(f"{z+1}:bookname: {target.targetfound[z]['bookname']}, isbn: {target.targetfound[z]['isbn']}, book code: {target.targetfound[z]['bookcode']}, author: {target.targetfound[z]['author']}, publisher: {target.targetfound[z]['publisher']}")
                    while True:
                        choice = input("check on some of the book information in detail?type the index or type No")
                        if choice != "No":
                            OutputUI(target.targetfound[choice-1])
                        else:
                            break
                    choice = input("Next page?type the Yes or No")
                    if choice == "No":
                        return
                temp_check = check
                for k in target.targetcondition:
                    for m in range(len(target.targetcondition[k])):
                        for n in range(len(bookinfo.hashmap[i][j][1][k])):
                            if target.targetcondition[k][m] == bookinfo.hashmap[i][j][1][k][n]:
                                temp_check -= 1
                                if k == "author":
                                    target.authorfound[m] += [bookinfo.hashmap[i][j][1]]
                if temp_check == 0:
                    target.targetfound += [bookinfo.hashmap[i][j][1]]
                if temp_check == 1:
                    target.subtargetfound += [bookinfo.hashmap[i][j][1]]
    if (len(target.targetfound)/2) < 20:
        for z in range(len(target.targetfound)):
            print(f"{z+1}: bookname: {target.targetfound[z]['bookname']}, isbn: {target.targetfound[z]['isbn']}, book code: {target.targetfound[z]['bookcode']}, author: {target.targetfound[z]['author']}, publisher: {target.targetfound[z]['publisher']}")
        while True:
            choice = input("check on some of the book information in detail?type the index or type No")
            if choice != "No":
                choice = int(choice)
                OutputUI(target.targetfound[choice-1])
            else:
                break
    choice = input("more?type the Yes or No")
    if choice == "Yes":
        if len(target.subtargetfound) >= 1:
            print("here are some books that is similar")
            finish = False
            n = len(target.subtargetfound)
            max = (math.ceil(n/10))*10
            min = (math.floor(n/10))*10
            count = (math.floor(n/10))*10
            if count == 0:
                max = n
            print(max,min,count)
            while not finish and count >= 0:
                for z in range(min-count, max-count):
                    print(f"{z+1}:bookname: {target.subtargetfound[z]['bookname']}, isbn: {target.subtargetfound[z]['isbn']}, book code: {target.subtargetfound[z]['bookcode']}, author: {target.subtargetfound[z]['author']}, publisher: {target.subtargetfound[z]['publisher']}")
                while True:
                    choice = input("check on some of the book information in detail?type the index or type No")
                    if choice != "No":
                        OutputUI(target.authorfound[choice-1])
                    else:
                        break
                count -= 10
                if count == 0:
                    max = n
                choice = input("next page?Yes/No ")
                if choice == "No":
                    finish = True
        elif len(target.authorfound) >= 1:
            print("here are some books with the same author")
            finish = False
            n = len(target.authorfound)
            max = (math.ceil(n/10))*10
            min = (math.floor(n/10))*10
            count = (math.floor(n/10))*10
            if count == 0:
                max = n
            while not finish:
                for z in range(min-count, max-count):
                    print(f"{z+1}:bookname: {target.authorfound[z]['bookname']}, isbn: {target.authorfound[z]['isbn']}, book code: {target.authorfound[z]['bookcode']}, author: {target.authorfound[z]['author']}, publisher: {target.authorfound[z]['publisher']}")
                while True:
                    choice = input("check on some of the book information in detail?type the index or type No")
                    if choice == "Yes":
                        OutputUI(target.authorfound[choice-1])
                    else:
                        break
                count -= 10
                if count == 0:
                    max = n
        else:
            print("no more similar result")
        print("all result is shown")