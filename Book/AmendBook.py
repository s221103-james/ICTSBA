import json
from Book.DataFileInitialisation import BookDataHashmapinitialise

def DeleteBook():
    with open("data/BookInfo.json") as bookinfofile:
        data = json.load(bookinfofile)
        bookinfo = BookDataHashmapinitialise()

    with open("data/BookStatus.json") as bookstatusfile:
        data = json.load(bookstatusfile)
    bookstatus = BookDataHashmapinitialise(data)


    target = input("please input the book code of the book you want to amend")
    targetindex = target[4:-2]
    for i in range(len(bookinfo[targetindex])):
        if bookinfo[targetindex][i][1]["bookcode"] == target:
            print(f"bookname: {bookinfo[targetindex][i][1]['bookname']}")
            print(f"isbn: {bookinfo[targetindex][i][1]['isbn']}")
            print(f"book code: {bookinfo[targetindex][i][1]['bookcode']}")
            print(f"author: {bookinfo[targetindex][i][1]['author']}")
            print(f"publisher: {bookinfo[targetindex][i][1]['publisher']}")
            print(f"bookcopies: {bookinfo[targetindex][i][1]['bookcopies']}")
            print(f"language; {bookinfo[targetindex][i][1]['language']}")
            print(f"publisheddate: {bookinfo[targetindex][i][1]['publisheddate']}")
            print(f"categories: {bookinfo[targetindex][i][1]['categories']}")
            print(f"averageRating: {bookinfo[targetindex][i][1]['averageRating']}")
            print(f"pagecount: {bookinfo[targetindex][i][1]['pagecount']}")
            print(f"descirption: {bookinfo[targetindex][i][1]['descirption']}")
            print(f":book available {bookinfo[targetindex][i][1]['available']}")
    print("type N/A if there is no need to change the data")
    tempbookinfo = {}
    print("input the book info that you want to change")
    tempbookinfo["bookname"] = input(f"book name: ")
    tempbookinfo["isbn"] = input(f"isbn code: ")
    tempbookinfo["bookcode"] = input(f"book code: ")
    tempbookinfo["author"] = input(f"author: ")
    tempbookinfo["publisher"] = input(f"publisher: ")
    tempbookinfo["bookcopies"] = input(f"book copies: ")
    tempbookinfo["language"] = input(f"book language: ")
    tempbookinfo["publisheddate"] = input(f"published date: ")
    tempbookinfo["categories"] = input(f"categories: ")
    tempbookinfo["averageRating"] = input(f"average rating: ")
    tempbookinfo["pagecount"] = input(f"page count: ")
    tempbookinfo["descirption"] = input(f"desciption: ")
    for i in tempbookinfo:
        if i != "N/A":
            bookinfo[targetindex][i][1][i] = tempbookinfo[i]
    print("Done")