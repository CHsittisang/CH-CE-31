const wapper = document.querySelector('.wapper');
const popup = document.querySelector('.popup');
const loginLink = document.querySelector('.registerLink');
const registerLink = document.querySelector('.loginLink');

const loginmenu = document.querySelector('.login-menu-btn');
const closeloginmenu = document.querySelector('.close');

registerLink.addEventListener('click', () => {
    wapper.classList.remove('active');
});

loginLink.addEventListener('click', () => {
    wapper.classList.add('active') ;
});

loginmenu.addEventListener('click', () => {
    popup.classList.add('active') 
});

closeloginmenu.addEventListener('click', () => {
    popup.classList.remove ('active'),
    wapper.classList.remove('active');
});


