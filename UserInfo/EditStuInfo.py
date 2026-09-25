import pandas as pd

def EditStuInfo(): 
    print("please input student info that is known")
    schiname = str.strip(input("student ID :"))
    sengname = str.strip(input("student ID :"))
    sclass = str.strip(input("student ID :").upper())
    sclassno = str.strip(input("student ID :"))
    if len(sclassno) == 1:
        sclassno = "0" + sclassno
    sid = str.strip(input("student ID :"))
    student = str.strip(input())


EditStuInfo()