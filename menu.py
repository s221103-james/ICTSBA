import csv
import pandas as pd
import os
from UserInfo.AddStuInfo import NewStudentInfo, AddStudentInfo
from Book.AddBook import AddBook

def menu():
    print(
        "1. search books\n"
        "2. borrow books\n"
        "3. check borrowing record\n"
        "4. admin\n"
        "5. bug report\n"
    )
    choice = str.strip(input("please input your option by typing the number"))
    match choice:
        case n if n== "1":
            ...
        case n if n == "2":
            ...
        case n if n == "3":
            ...
        case n if n == "4":
            print(
                "1. user information\n"
                "2. Add new books\n"
                "3. Update/Edit Books' information\n"
                "4. Delete book information"
            )
            choice = str.strip(input("please input your option by typing the number"))
            match choice :
                case n if n == "1":
                    print(
                        "1. Add student info\n"
                        "2. Edit student info\n"
                        "3. delete student info\n"
                        "4. Add teacher info\n"
                        "5. Edit teacher info\n"
                        "6. delete teacher info\n"
                        "7. student info yearly update\n"
                    )
                    choice = str.strip(input("please input your option by typing the number"))
                    match choice :
                        case n if n == "1":
                            print(
                                "1. add missing student\n"
                                "2. add new student"
                            )
                            choice = str.strip(input("please input your option by typing the number"))
                            print(choice)
                            AddStudentInfo(choice)
                        case n if n == "2":
                            ...
                case n if n == "2":
                    AddBook()
menu()      