from js import document
from pyodide.ffi import create_proxy

def handle_submit(e):
    e.preventDefault()

submit_proxy = create_proxy(handle_submit)
dataform = document.querySelector("booksearchinputbox")
dataform.addEventListener("submit", submit_proxy)