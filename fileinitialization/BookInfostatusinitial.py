import json

bookdata = []

for _ in range(30000):
    bookdata += [[]]

with open("data/BookInfo.json","w") as file:
    json.dump(bookdata, file, indent=3)

with open("data/BookStatus.json","w") as file:
    json.dump(bookdata, file, indent=3)