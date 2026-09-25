import json
from Book.DataFileInitialisation import BookDataHashmapinitialise

def DeleteBook():
    with open("data/BookInfo.json") as bookinfofile:
        data = json.load(bookinfofile)
        bookinfo = BookDataHashmapinitialise()

    with open("data/BookInfo.json") as bookinfofile:
        data = json.load(bookinfofile)
        bookinfo = BookDataHashmapinitialise(data)

    with open("data/BookStatus.json") as bookstatusfile:
        data = json.load(bookstatusfile)
    bookstatus = BookDataHashmapinitialise(data)


    target = input("please input the book code of the book you want to delete")
    targetindex = target[4:-2]
    for i in range(len(bookinfo[targetindex])):
        if bookinfo[targetindex][i][1]["bookcode"] == target:
            for j in range(i,len(bookinfo[targetindex])-1):
                bookinfo[targetindex][j] = bookinfo[targetindex][j+1]
            bookinfo[targetindex][j+1] = [None]
    print("Done")