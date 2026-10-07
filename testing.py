import requests
import csv

headers = {"User-Agent": "BookInfo (s221103@sttss.edu.hk)"} #enter the sch staff email
apikey  = "AIzaSyDVvbCUM8MBZjQNns-7oHeAQFhAXQW2uZE"
url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{9789887497981}&key={apikey}"
try:
    response = requests.get(url, headers=headers, timeout= 10)
    data = response.json()
    if "items" in data:
        book_info = data["items"][0]["volumeInfo"]
        bookname = book_info.get("title")
        bookcodelanguage_temp = book_info.get("language")
        if bookcodelanguage_temp[0:2] == "en":
            bookcodelanguage_temp = "e"
        elif bookcodelanguage_temp[0:2] == "zn":
            bookcodelanguage_temp = "c"
        else:
            bookcodelanguage_temp = "o"
        author = book_info.get("authors")
        publisher = book_info.get("publisher")
        publishedDate = book_info.get("publishedDate")
        language = book_info.get("language")
        pageCount = book_info.get("pageCount")
        if pageCount == 0:
            pageCount = "N/A"
        categories = book_info.get("categories")
        averageRating = book_info.get("averageRating")
        if averageRating == None:
            averageRating = "N/A"
        description = book_info.get("description")
        if description == None:
            description = "N/A"
        print("bookname")
    elif "error" in data:
        apikey = (input("Invalid api key, please re-enter it")).strip()
    elif "None" in data:
        print("asd")
    else:
        found = True
        print(data)
        bookname,bookcode,author,publisher,bookcopies,language,publishedDate,categories,averageRating,pageCount,description = None ,None, None, None, None, None, None, None, None, None, None
except requests.exceptions.RequestException as error:
    print("Network Error, please try again")
except requests.exceptions.ConnectionError as error:
    print("Connection Error, please ret again")