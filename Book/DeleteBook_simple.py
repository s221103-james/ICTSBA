import json
from DataFileInitialisation import BookDataHashmapinitialise

def DeleteBook():
    with open("data/BookInfo.json") as bookinfofile:
        data = json.load(bookinfofile)
        bookinfo = BookDataHashmapinitialise(data)

    with open("data/BookStatus.json") as bookstatusfile:
        data = json.load(bookstatusfile)
    bookstatus = BookDataHashmapinitialise(data)

    checkindex = input("please input the book code of the book you want to delete")
    checkindexisbn = checkindex[4:-2]
    for i in range(len(bookinfo[checkindexisbn])):
        if bookinfo[checkindexisbn][i][1]["bookcode"] == checkindex:
            checkindexisbn2 = i
    print(bookinfo[checkindexisbn])
    for j in range(checkindexisbn2,len(bookinfo[checkindexisbn])-1):
        bookinfo[checkindexisbn][j][1] = bookinfo[checkindexisbn][j+1][1]
    bookinfo[checkindexisbn][-1] = [None]
    print("Done")
    print(bookinfo[checkindexisbn])
    with open("data/BookInfo.json","w") as BookInfoData:
        json.dump(bookinfo.hashmap, BookInfoData, indent=3)