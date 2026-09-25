import json

from DataFileInitialisation import BookDataHashmapinitialise
from AddBook_simple import AddBookData

class BookData:
    def __init__(self,bookname,bookcode,isbn,author,publisher,bookcopies,language,publishedDate,categories,averageRating,pageCount):
        self.targetcondition = {}
        self.bookname = bookname
        self.bookcode = bookcode
        self.isbn = isbn
        #self.author = author
        if author != "N/A":
            self.targetcondition["author"] = author
        if publisher != "N/A":
            self.targetcondition["publisher"] = publisher
        if publishedDate != "N/A":
            self.targetcondition["publishedDate"] = publishedDate
        if language != "N/A":
            self.targetcondition["language"] = language
        if categories != "N/A":
            self.targetcondition["categories"] = categories
        if averageRating != "N/A":
            self.targetcondition["averageRating"] = averageRating
        if bookcopies != "N/A":
            self.targetcondition["bookcopies"] = bookcopies
        if pageCount != "N/A":
            self.targetcondition["pageCount"] = pageCount
        
        #self.publisher = publisher
        #self.publishedDate = publishedDate
        #self.language = language
        #self.categories = categories
        #self.averageRating = averageRating
        #self.bookcopies = bookcopies
        #self.pageCount = pageCount

    @classmethod
    def get(cls):
        bookname = input("bookname: ")
        bookcode = input("bookcode: ")
        isbn = input("isbn: ")
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
    print(f"publisheddate: {z['publisheddate']}")
    print(f"categories: {z['categories']}")
    print(f"averageRating: {z['averageRating']}")
    print(f"pagecount: {z['pagecount']}")
    print(f"descirption: {z['descirption']}")
    print(f":book available {z['available']}")
def finding(target):
    global bookinfo
    targetfound = []
    subtargetfound = []
    authorfound = []
    checkall = 0
    for z in target.targetcondition:
        checkall += len(target.targetcondition[z])
    for i in range(len(bookinfo)):
        for j in range(len(bookinfo[i])):
            if len(targetfound) %10 == 0 and len(targetfound) >= 0:
                for z in range(len(targetfound)-20, len(targetfound)-9):
                    print(f"{z+1}:bookname: {targetfound[z]['bookname']}, isbn: {targetfound[z]['isbn']}, book code: {targetfound[z]['bookcode']}, author: {targetfound[z]['author']}, publisher: {targetfound[z]['publisher']}")
                while True:
                    choice = input("check on some of the book information in detail?type the index or type No")
                    if choice != "No":
                        OutputUI(targetfound[choice-1])
                    else:
                        break
                choice = input("Next page?type the Yes or No")
                if choice == "No":
                    return targetfound, subtargetfound, authorfound
            checkalltemp = checkall
            for k in target.targetcondition:
                for n in target.targetcondition[k]:
                    for m in bookinfo[i][j][1][k]:
                        if m == n:
                            checkalltemp -= 1
            if checkalltemp == 0:
                bookinfo[i][j][1]["available"] = 0
                if bookinfo[i][j][1]["status"] == "a":
                    bookinfo[i][j][1]["available"] += 1
                if len(targetfound) >= 1:
                    if bookinfo[i][j][1]["isbn"] == targetfound[-1]["isbn"]:
                        targetfound[-1]["bookcode"] = [targetfound[-1]["bookcode"], bookinfo[i][j][1]["bookcode"]]
                        targetfound[-1]["available"] += bookinfo[i][j][1]["available"]
                    else:
                        targetfound += bookinfo[i][j][1]
                else:
                    targetfound += bookinfo[i][j][1]
            elif checkalltemp == 1 and checkall > 1:
                bookinfo[i][j][1]["available"] = 0
                if bookinfo[i][j][1]["status"] == "a":
                    bookinfo[i][j][1]["available"] += 1
                if len(subtargetfound) >= 1:
                    if bookinfo[i][j][1]["isbn"] == subtargetfound[-1]["isbn"]:
                        subtargetfound[-1]["bookcode"] = [subtargetfound[-1]["bookcode"], bookinfo[i][j][1]["bookcode"]]
                        subtargetfound[-1]["available"] += bookinfo[i][j][1]["available"]
                    else:
                        subtargetfound += bookinfo[i][j][1]
                else:
                    subtargetfound += bookinfo[i][j][1]
            if "author" in target.targetcondition:
                if bookinfo[i][j][1]["author"] == target.targetcondition["author"]:
                    bookinfo[i][j][1]["available"] = 0
                    if bookinfo[i][j][1]["status"] == "a":
                        bookinfo[i][j][1]["available"] += 1
                    if len(authorfound) >= 1:
                        if bookinfo[i][j][1]["isbn"] == authorfound[-1]["isbn"]:
                            authorfound[-1]["bookcode"] = [authorfound[-1]["bookcode"], bookinfo[i][j][1]["bookcode"]]
                            authorfound[-1]["available"] += bookinfo[i][j][1]["available"]
                        else:
                            authorfound += bookinfo[i][j][1]
                    else:
                        authorfound += bookinfo[i][j][1]     
    return targetfound, subtargetfound, authorfound

def ReadBook():
    with open("data/BookInfo.json") as bookinfofile:
        data = json.load(bookinfofile)
    bookinfo = BookDataHashmapinitialise(data)

    with open("data/BookStatus.json") as bookstatusfile:
        data = json.load(bookstatusfile)
    bookstatus = BookDataHashmapinitialise(data)

    print("type N/A if you don't know the info")
    target = BookData.get()

    #bookcode
    if target.bookcode != "N/A":
        if target.isbn == "N/A":
            targetindex = target.bookcode[4:-2]
        else:
            targetindex = target.isbn
        for i in bookinfo[targetindex]:
            if i[1]["bookcode"] == target.bookcode:
                targetfound += [i[1]]
            if i[1]["isbn"] == targetindex:
                subtargetfound += [i[1]]
            
    #isbn
    elif target.isbn != "N/A":
        targetindex = target.isbn
        for i in bookinfo[targetindex]:
            if i[1]["bookcode"] == target.bookcode:
                targetfound += [i[1]]

    #others
    else:
        targetfound, subtargetfound, authorfound = finding(target)
        if len(targetfound) < 20:
            for z in range(1,20):
                print(f"{z+1}:bookname: {targetfound[z]['bookname']}, isbn: {targetfound[z]['isbn']}, book code: {targetfound[z]['bookcode']}, author: {targetfound[z]['author']}, publisher: {targetfound[z]['publisher']}")
                while True:
                    choice = input("check on some of the book information in detail?type the index or type No")
                    if choice != "No":
                        OutputUI(targetfound[choice-1])
                    else:
                        break
                while True:
                    i = len(subtargetfound)
                    j = len(authorfound)
                    choice = input("more?type the Yes or No")
                    if choice == "No":
                        break
                    elif choice == "yes":
                        if len(subtargetfound) >= 1:
                            print("here are some books that is similar")
                            for z in range(len(subtargetfound)):
                                print(f"{z+1}:bookname: {authorfound[z]['bookname']}, isbn: {subtargetfound[z]['isbn']}, book code: {subtargetfound[z]['bookcode']}, author: {subtargetfound[z]['author']}, publisher: {subtargetfound[z]['publisher']}")
                                while True:
                                    choice = input("check on some of the book information in detail?type the index or type No")
                                    if choice != "No":
                                        OutputUI(authorfound[choice-1])
                                    else:
                                        break
                        elif len(authorfound) >= 1:
                            for z in range(len(authorfound)):
                                print("here are some books with the same author")
                                print(f"{z+1}:bookname: {authorfound[z]['bookname']}, isbn: {authorfound[z]['isbn']}, book code: {authorfound[z]['bookcode']}, author: {authorfound[z]['author']}, publisher: {authorfound[z]['publisher']}")
                                while True:
                                    choice = input("check on some of the book information in detail?type the index or type No")
                                    if choice != "No":
                                        OutputUI(authorfound[choice-1])
                                    else:
                                        break
                        else:
                            print("no more similar result")
    with open("data/BookInfo.json","w") as BookInfoData:
       json.dump(bookinfo.hashmap, BookInfoData, indent=3)
    with open("data/BookStatus.json", "w") as BookStatusFile:
        json.dump(bookstatus.hashmap, BookStatusFile, indent=3)
