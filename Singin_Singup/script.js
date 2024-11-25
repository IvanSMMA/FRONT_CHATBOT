const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');
const change1=document.getElementById('changeup');
const change2=document.getElementById('changein');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

change1.addEventListener('click', () => {
    container.classList.add("active");
});

change2.addEventListener('click', () => {
    container.classList.remove("active");
});


const signInForm = document.getElementById('signInForm');
const signInBtn = document.getElementById('signInBtn');

signInBtn.addEventListener('click', function(event) {

const email = signInForm.querySelector('#mailin').value;
const password = signInForm.querySelector('#contrain').value;


if (!email || !password) {
    alert('Please complete the text fields ');
    event.preventDefault(); 
} else {
    alert('Welcome again');
}
});

const signupForm = document.getElementById('signupForm');
const signupBtn = document.getElementById('signupBtn');

signupBtn.addEventListener('click', function(event) {

const emailup = signupForm.querySelector('#mail').value;
const passwordup = signupForm.querySelector('#contra').value;


if (!emailup || !passwordup) {
    alert('Please complete the text fields ');
    event.preventDefault(); 
} else {
    alert('Account successfully registered');
}
});