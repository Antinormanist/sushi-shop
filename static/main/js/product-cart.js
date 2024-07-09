const minus = document.querySelector('.minus')
const plus = document.querySelector('.plus')
const amount = document.querySelector('.num')
const priceOrigin = parseInt(document.querySelector('.price').innerText.split('р')[0])
const price = document.querySelector('.price')
const bttn = document.querySelector('.add-to-cart')

window.addEventListener('click', function(event) {
    if (event.target === minus && parseInt(amount.innerText) > 1) {
        --amount.innerText
    } else if (event.target === plus && parseInt(amount.innerText) < 999) {
        ++amount.innerText
    } else if (event.target === bttn) {
        amount.innerText = 1
        // Do whatever you want
    }

    price.innerText = priceOrigin * parseInt(amount.innerText) + 'руб.'
})