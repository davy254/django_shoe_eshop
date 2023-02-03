const updateBtns = document.querySelectorAll('.update-cart');
console.log(updateBtns);

updateBtns.forEach(btn => {
    btn.addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId: ', productId, 'Action: ', action)
    });
});

console.log('USER: ', user)

user === 'Anonymous' ?  console.log('User is not authenticated') : console.log('User is authenticated, sending data...')