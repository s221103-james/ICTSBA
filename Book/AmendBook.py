import json
from DataFileInitialisation import BookDataHashmapinitialise

def AmendBook():
    with open("data/BookInfo.json") as bookinfofile:
        data = json.load(bookinfofile)
        bookinfo = BookDataHashmapinitialise(data)

    checkindex = input("please input the bookcode of the book that you can to check(one at a time)")
    checkindexisbn = checkindex[4:-2]
    for i in range(len(bookinfo[checkindexisbn])):
        if bookinfo[checkindexisbn][i][1]["bookcode"] == checkindex:
            checkindexisbn2 = i
    print("type N/A if there is no need to change the data")
    tempbookinfo = {}
    tempbookinfo["bookname"] = input(f"book name: {bookinfo[checkindexisbn][checkindexisbn2][1]['bookname']}")
    tempbookinfo["isbn"] = input(f"isbn code: {bookinfo[checkindexisbn][checkindexisbn2][1]['isbn']}")
    tempbookinfo["bookcode"] = input(f"book code: {bookinfo[checkindexisbn][checkindexisbn2][1]['bookcode']}")
    tempbookinfo["author"] = input(f"author: {bookinfo[checkindexisbn][checkindexisbn2][1]['author']}")
    tempbookinfo["publisher"] = input(f"publisher: {bookinfo[checkindexisbn][checkindexisbn2][1]['publisher']}")
    tempbookinfo["bookcopies"] = input(f"book copies: {bookinfo[checkindexisbn][checkindexisbn2][1]['bookcopies']}")
    tempbookinfo["language"] = input(f"book language: {bookinfo[checkindexisbn][checkindexisbn2][1]['language']}")
    tempbookinfo["publishedDate"] = input(f"published date: {bookinfo[checkindexisbn][checkindexisbn2][1]['publishedDate']}")
    tempbookinfo["categories"] = input(f"categories: {bookinfo[checkindexisbn][checkindexisbn2][1]['categories']}")
    tempbookinfo["averageRating"] = input(f"average rating: {bookinfo[checkindexisbn][checkindexisbn2][1]['averageRating']}")
    tempbookinfo["pageCount"] = input(f"page count: {bookinfo[checkindexisbn][checkindexisbn2][1]['pageCount']}")
    tempbookinfo["description"] = input(f"desciption: {bookinfo[checkindexisbn][checkindexisbn2][1]['description']}")

    for i in bookinfo[checkindexisbn][checkindexisbn2][1]:
        if tempbookinfo[i] != "N/A":
            bookinfo[checkindexisbn][checkindexisbn2][1][i] = tempbookinfo[i]
    
    print("Done")
