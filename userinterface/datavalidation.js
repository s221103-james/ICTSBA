const form = document.getElementById('booksearchinputbox')
const bookname = document.getElementById('bookname')
const bookcode = document.getElementById('bookcode')
const isbn = document.getElementById('isbn')
const author = document.getElementById('author')
const publisher = document.getElementById('publisher')
const publishedate = document.getElementById('publishedate')
const language = document.getElementById('language')
const catergories = document.getElementById('catergories')
const averagerating = document.getElementById('averagerating')
const bookcopies = document.getElementById('bookcopies')
const pagecount = document.getElementById('pagecount')

form.addEventListener('submit', (e) =>{
    e.preventDefault();

    validation();
})

const SetError = (element, message) =>{
    const InputControl= element.parentElement;
    const ErrorDisplay = InputControl.querySelector('.failed');

    failedDisplay.innerText = message;
    InputControl.classList.add('failed');
    InputControl.classList.remove('success')
}

const SetSuccess = (element, message) =>{
    const InputControl= element.parentElement;
    const ErrorDisplay = InputControl.querySelector('.failed');

    failedDisplay.innerText = message;
    InputControl.classList.remove('failed');
    InputControl.classList.add('success')
}

const validation = () => {
    const booknameValue = bookname.value.trim();
    const bookcodeValue = bookcode.value.trim();
    const isbnValue = isbn.value.trim();
    const authorValue = author.value.trim();
    const publisherValue = publisher.value.trim();
    const publishedateValue = publishedate.value.trim();
    const languageValue = language.value.trim();
    const catergoriesValue = catergories.value.trim();
    const averageratingValue = averagerating.value.trim();
    const bookcopiesValue = bookcopies.value.trim();
    const pagecountValue = pagecount.value.trim();

    if(booknameValue === '') {
        SetError(bookname, 'Book Name is required');
    } else{
        SetSuccess(bookname);
    }
};

