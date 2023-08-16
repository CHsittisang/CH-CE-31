// searchform
let searchForm = document.querySelector('.search-form');
document.querySelector('#search-bth').onclick =() =>{
    searchForm.classList.toggle('active');
    shoppingCart.classList.remove('active');
    loginForm.classList.remove('active');
    navbar.classList.remove('active');
}

// shopping-cart
let shoppingCart = document.querySelector('.shopping-cart');
document.querySelector('#cart-bth').onclick =() =>{
    shoppingCart.classList.toggle('active');
    searchForm.classList.remove('active');
    loginForm.classList.remove('active');
    navbar.classList.remove('active');
}

// login-form
let loginForm = document.querySelector('.login-form');
document.querySelector('#user-bth').onclick =() =>{
    loginForm.classList.toggle('active');
    searchForm.classList.remove('active');
    shoppingCart.classList.remove('active');
    navbar.classList.remove('active');
}

// menu-bar
let navbar = document.querySelector('.navbar');
document.querySelector('#menu-bth').onclick =() =>{
    navbar.classList.toggle('active');
    searchForm.classList.remove('active');
    shoppingCart.classList.remove('active');
    loginForm.classList.remove('active');
}

window.onscroll =() =>{
    searchForm.classList.remove('active');
    shoppingCart.classList.remove('active');
    loginForm.classList.remove('active');
    navbar.classList.remove('active');
}

