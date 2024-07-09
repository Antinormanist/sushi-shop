const btn = document.querySelector('.comment-read')
const views = document.querySelector('.user-views')

btn.addEventListener('click', function() {
    if (views.classList.contains('none')) {
        views.classList.remove('none')
        views.classList.add('grid')
        btn.innerText = 'Сверхнуть отзывы'
    } else {
        views.classList.remove('grid')
        views.classList.add('none')
        btn.innerText = 'Читать отзывы'
    }
})