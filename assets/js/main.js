const menu_open = document.getElementById('menu');
const menu_close = document.getElementById('menu_close');
const top_bar = document.getElementById('top-bar');
const searchbar_close = document.getElementById('search-bar-close');
const searchbar_open = document.getElementById('search-bar-open');
const searchbar = document.getElementById('search-bar');
const category = document.getElementById('category');
const categorylist = document.getElementById('categorylist');
const down = document.getElementById('down');
const body = document.getElementsByTagName('header');
const navItemHome = document.getElementById('nav-item-home')
const navItemList = document.getElementById('nav-item-list')
// const eye_control = document.querySelectorAll('#eye-control');


const customer_slider = document.querySelector('.clients-list');
const product_slider = document.querySelector('#slider');
const article_slider = document.querySelector('.product-list.slider');
let isDown = false;
let startX;
let scrollLeft;

var click_counter = 0
function display_sleep(){
    if(top_bar.style.display=="none"){
        top_bar.style.display="flex";
    }else{
        top_bar.style.display="none";
    }
     
}
category.addEventListener('mouseenter', () => {
    categorylist.style.display = 'flex';
    categorylist.style.zIndex = '999';
    down.style.transform = 'rotateZ(220deg)';
    setTimeout(() => {
    categorylist.style.opacity = '1';


    }, 300);
})
category.addEventListener('click', () => {
    if(click_counter===0){
        categorylist.style.display = 'flex';
        categorylist.style.opacity = '1';
        down.style.transform = 'rotateZ(220deg)';
        click_counter++;
    }else{
        categorylist.style.display = 'none';
        categorylist.style.opacity = '0';
        down.style.transform = 'rotateZ(45deg)';
        click_counter--;
    }
})
category.addEventListener('mouseleave', () => {
    if(!isEntered){
        categorylist.style.display = 'none';
        categorylist.style.opacity = '0';
    down.style.transform = 'rotateZ(45deg)';
    }
})
categorylist.addEventListener('mouseenter', () => {
    categorylist.style.display = 'flex';
    categorylist.style.opacity = '1';
    categorylist.classList.add('entered');
})

categorylist.addEventListener('mouseleave', () => {
    categorylist.style.opacity = '0';
    categorylist.classList.remove('entered');
    setTimeout(() => {
        categorylist.style.display = 'none';

    }, 500);
    
    down.style.transform = 'rotateZ(45deg)';
})



navItemHome.addEventListener('mouseenter', () =>{
        categorylist.style.opacity = '0';
    categorylist.classList.remove('entered');
        down.style.transform = 'rotateZ(45deg)';
    setTimeout(() => {
        categorylist.style.display = 'none';

    }, 500);
})
navItemList.addEventListener('mouseenter', () =>{
        categorylist.style.opacity = '0';
    categorylist.classList.remove('entered');
        down.style.transform = 'rotateZ(45deg)';
    setTimeout(() => {
        categorylist.style.display = 'none';

    }, 500);

})
function isEntered() {
    return categorylist.classList.contains('entered');
}
// eye_control.addEventListener('click', () =>{
//     eye_control.classList.add('choosed')
//     product_image.style.display = 'flex';
//     console.log(eye_control.classList.contains('choosed'));
// })
// product_image_close.addEventListener('mousedown', () =>{

//     product_image.style.display = 'none';
// })


menu_close.addEventListener('click', () => {
    
    
    top_bar.style.transform ='translateX(100%)';
    top_bar.style.transition ='transform .3s ease-in-out';
    setTimeout(() => {
            top_bar.style.display="none";

    }, 300);
})

menu_open.addEventListener('click', () => {
    document.documentElement.style.height = '0';
    document.documentElement.style.overflow = 'hidden';
    // top_bar.style.transition = "left 1s ease-in";
    top_bar.style.display ='flex';
    
    setTimeout(() => {
        top_bar.style.transform ='translateX(0)';

}, 100);


})
searchbar_close.addEventListener('click', () => {
    
    searchbar.style.transform ='translateY(-100%)';


});
searchbar_open.addEventListener('click', () => {
    
    searchbar.style.transform ='translateY(0)';
    searchbar.style.position ='fixed';
});

customer_slider.addEventListener('mousedown', (e) => {
    e.preventDefault();
    isDown = true;
    customer_slider.classList.add('activeS');
    startX = e.pageX;
    console.log(startX);
});
customer_slider.addEventListener('mouseleave', () => {
    isDown = false;
    customer_slider.classList.remove('activeS');
});
customer_slider.addEventListener('mouseup', () => {
    isDown = false;
    customer_slider.classList.remove('activeS');
});
customer_slider.addEventListener('mousemove', (e) => {
    if(!isDown)return;
    e.preventDefault();
    const X = e.pageX;
    const walk = (X - startX)/10;
    customer_slider.scrollLeft -= walk;
});

article_slider.addEventListener('mousedown', (e) => {
    e.preventDefault();
    isDown = true;
    article_slider.classList.add('activeS');
    startX = e.pageX;
    console.log(startX);
});
article_slider.addEventListener('mouseleave', () => {
    isDown = false;
    article_slider.classList.remove('activeS');
});
article_slider.addEventListener('mouseup', () => {
    isDown = false;
    article_slider.classList.remove('activeS');
});
article_slider.addEventListener('mousemove', (e) => {
    if(!isDown)return;
    e.preventDefault();
    const X = e.pageX;
    const walk = (X - startX) *2;
    article_slider.scrollLeft -= walk;
});

