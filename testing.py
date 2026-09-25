import requests
import csv

with open("testing.csv","r") as file:
    a = list(csv.reader(file))
print(a)

print()

print(['empty']*4)