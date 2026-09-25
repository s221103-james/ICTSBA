import pandas as pd
import csv

from datetime import datetime

class Target :
    def __init__(self, schiname, sengname, sclass, sclassno, sid):
        self.schiname = schiname
        self.sengname = sengname
        self.sclass = sclass
        self.sclassno = sclassno
        self.sid = sid

    def to_dict(self) -> dict:
        return {"sid": self.sid, "chiname": self.schiname, "engname": self.sengname, "sclass": self.sclass, "sclassno": self.sclassno}

    @classmethod
    def GetTargetInfo(cls):
        schiname = str.strip(input("Student chinese name: "))
        sengname = str.strip(input("Student English name: "))
        sclass = str.strip((input("Student class: ")).upper())
        if len(sclass) == 2:
            sclass = sclass[0] + (sclass[1]).encode('ascii').hex()[1]
        sclassno = str.strip(input("Student class number: ") )
        if len(sclassno) == 1:
            sclassno = "0" + sclassno
        sid = input("Student ID: ")

def stusearch():
    ClassDataFieldnames = ["class","number of student","number of books borrowed"]
    StudentInfoFieldnames = ["sid", "schiname", "sengname", "sclass"]
    target = Target.GetTargetInfo()
    result = []
    with open("StudentInfo.csv","r") as StuInfoFile:
        StuInfo = list(csv.DictReader(StuInfoFile)) 
    with open("ClassData.csv","r") as ClsDataFile:
        ClsData = list(csv.DictReader(ClsDataFile))
    if target.sid != None:
        date = str(datetime.now())[0:7].replace("-", "")
        estimateformbase = int(date[0:4])- target.sid[1:3]
        if int(date[4:6]) > 8:
            estimateformbase += 1
        count = 1
        Found = False
        while (ClsData[count]["class"])[0] != estimateformbase and count <= 31: #no need to run through everything, it just search the A class
            n += ClsData["number of student"]
            count += 1
        while not Found:
            for i in range(6):
                expected_range += int(ClsData[count]["number of student"]) 
                count += 1
            for i in range(expected_range):
                if target.sid == StuInfo[count+i]["sid"]:
                    Found = True
                    target_index = count+i
                    result += [StuInfo[count+i]]
            if (count-12) > 0:
                count -= 11
            else:
                count = 31
    #estimate the student formbase now
    elif target.sclass != None and target.sclassno != None:
        with open("ClassData.csv","r") as StuInfoFile:
            reader = csv.DictReader(StuInfoFile)
            i = next(reader)
            i = next(reader)
            while int(i["class"]) < target.sclass:
                i = next(reader)
                target_index += int(i["number of student"])
        target_index += target.sclassno -1

    elif target.schiname != None and target.sengname != None:
        ...
        #find sth that matches both, if not print no matched person is found but still find them indepently
    elif target.sclass != None and target.sclassno != None:
        ...
    else:
        if target.sclass != None:
            ...
        if target.sclassno != None:
            ...
        if target.schiname != None:
            ...
        if target.sengname != None:
            ...
    
    #ordered by distinsiveness

stusearch()