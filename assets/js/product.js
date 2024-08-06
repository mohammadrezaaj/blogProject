const product_image = document.querySelectorAll('#product-image #eye-control').forEach(i =>{
    i.onclick = () =>{
        document.querySelector('.product-image').style.display = 'flex';
        document.querySelector('.product-image img').src=i.children[0].src;
    }
});
const product_image_close = document.getElementById('product-image-close').addEventListener('click', () =>{
    document.querySelector('.product-image').style.display = 'none';

});
console.log(product_image);
console.log(product_image_close);