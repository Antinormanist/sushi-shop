const burgerBtn = document.querySelector('.burger')
const burgerMenu = document.querySelector('.menu')
const burgerContainer = document.querySelector('.burger-container')

burgerBtn.addEventListener('click', function() {
    if (burgerMenu.classList.contains('menu-display')) {
        burgerContainer.classList.remove('burger-btn-bg')
        burgerMenu.classList.remove('menu-display')
    } else {
        burgerContainer.classList.add('burger-btn-bg')
        burgerMenu.classList.add('menu-display')
    }
})