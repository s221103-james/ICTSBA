import csv
import pandas as pd
import os

from datetime import datetime

def inputUI() :
    schiname = str.strip(input("Student chinese name: "))
    sengname = str.strip(input("Student English name: "))
    sclass = str.strip((input("Student class: ")).upper())
    sclassno = str.strip(input("Student class number: ") )
    if len(sclassno) == 1:
        sclassno = "0" + sclassno
    sid = input("Student ID: ")
    return schiname, sengname, sclass, sclassno, sid

def GetNewStuInfo():
    year = str(datetime.now())[2] + str(datetime.now())[3]
    Flag = False
    while not Flag:
        Flag = True
        schiname, sengname, sclass, sclassno, sid = inputUI()
        if not schiname or not sengname or not sclass or not sclassno or not sid :
            print("Missing information")
            Flag = False
        if len(sclass) == 2:
            sclass = sclass[0] + (sclass[1]).encode('ascii').hex()[1]
        else:
            print("Invaild student class format")
        if sclassno <= "00" :
            print('Invalid class number')
            Flag = False
        if year != sid[1:3] :
            print("Invalid student ID, year of entry and ID don't match")
            Flag = False
        if sclass != sid[3:5] and not sclass:
            print("Invalid student ID, student class and ID don't match")
            Flag = False
        if sclassno != sid[5:7]:
                print("Invalid student ID, student class number and ID don't match")
    return {"sid":sid, "schiname":schiname, "sengname":sengname, "sclass":sclass, "sclassno":sclassno}
def GetMissingSudentInfo():
    Flag = False
    while not Flag:
        Flag = True
        schiname, sengname, sclass, sclassno, sid = inputUI()
        if not schiname or not sengname or not sclass or not sclassno or not sid :
            print("Missing information")
            Flag = False
    return {"sid":sid, "schiname":schiname, "sengname":sengname, "sclass":sclass, "sclassno":sclassno}
    
def AddStudentInfo(choice):
    print(choice)
    match choice:
        case k if k == "1":
            student = GetMissingSudentInfo()
        case k if k =="2":
            student = GetNewStuInfo()
    n = int(student["sclass"][2:5])
    sclass = int(student["sid"][3:5])

    ClassDataFieldnames = ["class","number of student","number of books borrowed"]
    StudentInfoFieldnames = ["sid", "schiname", "sengname", "sclass"]

    with open("ClassData.csv","r") as StuInfoFile:
        reader = csv.DictReader(StuInfoFile)
        i = next(reader)
        i = next(reader)
        while int(i["class"]) < sclass:
            n += int(i["number of student"])
            i = next(reader)
    #find the index, minimise the time for sorting
    with open("StudentInfo.csv","r") as StuInfoFile :
        studentlist = list(csv.DictReader(StuInfoFile))

    studentlist.insert(n-1, student)

    #for i in range(Stunumber + 1, n, -1):
    #    temp = studentlist[i]
    #    studentlist[i] = studentlist[i-1]
    #    studentlist[i-1] = temp

    with open("StudentInfo.csv","w") as StuInfoFile :
        csv_writer = csv.DictWriter(StuInfoFile, fieldnames=StudentInfoFieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(studentlist)

    with (
        open("ClassData.csv","r") as original,
        open("ClassData_temp.csv","w") as new,
    ):
        reader = csv.DictReader(original)
        writer = csv.DictWriter(new, fieldnames=reader.fieldnames)

        writer.writeheader()

        for i in reader:
            if str(i["class"]) == "00" or str(i["class"]) == str(sclass):
               i["number of student"] = str(int(i["number of student"]) + 1)
            writer.writerow(i)
    os.replace("ClassData_temp.csv", "ClassData.csv")