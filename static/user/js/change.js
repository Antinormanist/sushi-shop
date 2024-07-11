const changeBtn = document.querySelector('.change-info')
const overlay = document.querySelector('.overlay')
const changeWindow = document.querySelector('.change-div')

window.addEventListener('click', function(event) {
    if (event.target === changeBtn) {
        overlay.classList.add('display')
        changeWindow.classList.add('display')
    } else if (event.target === overlay) {
        overlay.classList.remove('display')
        changeWindow.classList.remove('display')
    }
})