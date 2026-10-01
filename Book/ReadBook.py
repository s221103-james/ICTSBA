import json

from DataFileInitialisation import BookDataHashmapinitialise

class BookData:
    def __init__(self,bookname,bookcode,isbn,author,publisher,bookcopies,language,publishedDate,categories,averageRating,pageCount):
        self.targetcondition = {}
        self.bookname = bookname
        self.bookcode = bookcode
        self.isbn = isbn
        if author[0] != "N/A":
            self.targetcondition["author"] = author
            print("author")
        if publisher != "N/A":
            self.targetcondition["publisher"] = publisher
            print("publisher")
        if publishedDate != "N/A":
            self.targetcondition["publishedDate"] = publishedDate
            print("publishedDate")
        if language != "N/A":
            self.targetcondition["language"] = language
            print("language")
        if categories[0] != "N/A":
            self.targetcondition["categories"] = categories
            print("categories")
        if averageRating != "N/A":
            self.targetcondition["averageRating"] = averageRating
            print("averageRating")
        if bookcopies != "N/A":
            self.targetcondition["bookcopies"] = bookcopies
            print("bookcopies")
        if pageCount != "N/A":
            self.targetcondition["pageCount"] = pageCount
            print("pageCount")

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
def finding(target, bookinfo, bookstatus):
    targetfound = []
    subtargetfound = []
    authorfound = []
    checkall = len(target.targetcondition)
    for i in range(len(bookinfo.hashmap)):
        for j in range(len(bookinfo.hashmap[i])):
            checkalltemp = checkall
            for k in target.targetcondition:
                for n in target.targetcondition[k]:
                    for m in bookinfo.hashmap[i][j][1][k]:
                        if m == n:
                            checkalltemp -= 1
            if checkalltemp == 0:
                targetfound += [bookinfo.hashmap[i][j][1]]
                print(j)
                if bookstatus.hashmap[i][j][1]["status"] == "a":
                    temp = "1"
                targetfound[-1]["status"] = temp
            elif checkalltemp == 1 and checkall > 1:
                subtargetfound += [bookinfo.hashmap[i][j][1]]
                if bookstatus.hashmap[i][j][1]["status"] == "a":
                    temp = "1"
                subtargetfound[-1]["status"] = temp
            if "author" in target.targetcondition:
                    authorfound += [bookinfo.hashmap[i][j][1]]
                    if bookstatus.hashmap[i][j][1]["status"] == "a":
                        temp = "1"
                    authorfound[-1]["status"] = temp
            if len(targetfound) %10 == 0 and len(targetfound) >= 20:
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
    targetfound = []
    subtargetfound = []
    authorfound = []
    checkall = 0
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
            if i[1]["isbn"] == target.isbn:
                targetfound += [i[1]]

    #others
    else:
        targetfound, subtargetfound, authorfound = finding(target, bookinfo, bookstatus)
        if (len(targetfound)/2) < 20:
            print(4)
            for z in range(len(targetfound)):
                print(f"{z+1}: bookname: {targetfound[z]['bookname']}, isbn: {targetfound[z]['isbn']}, book code: {targetfound[z]['bookcode']}, author: {targetfound[z]['author']}, publisher: {targetfound[z]['publisher']}")
            while True:
                choice = input("check on some of the book information in detail?type the index or type No")
                if choice != "No":
                    choice = int(choice)
                    OutputUI(targetfound[choice-1])
                else:
                    break
        i = len(subtargetfound)
        j = len(authorfound)
        choice = input("more?type the Yes or No")
        if choice == "yes":
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
                        if choice == "Yes":
                            OutputUI(authorfound[choice-1])
                        else:
                            break
            else:
                print("no more similar result")