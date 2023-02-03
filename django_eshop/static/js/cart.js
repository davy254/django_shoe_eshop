const updateBtns = document.querySelectorAll('.update-cart');
console.log(updateBtns)

updateBtns.forEach(btn => {
    btn.addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId: ', productId, 'Action: ', action)
    })
});