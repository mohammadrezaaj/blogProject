const questions = document.querySelectorAll('.list ul li');

questions.forEach(i =>{
    i.onclick= () =>{
        if(i.nextElementSibling.children[0].classList.contains('visible') &&
        i.nextElementSibling.classList.contains('show')){
            i.nextElementSibling.style.transform = "scaleY(0)";
            setTimeout( () =>{
                i.nextElementSibling.style.height = 0;

                }, 1000);
            i.nextElementSibling.children[0].style.visibility = "hidden";
            i.nextElementSibling.children[0].classList.remove('visible');
            i.nextElementSibling.classList.remove('show');
            i.children[1].style.transform = "rotateZ(45deg)";


        }else{
            i.nextElementSibling.style.transition = "all 1s ease";
            i.nextElementSibling.children[0].style.transition = "all .1s ease"
            setTimeout( () =>{
            i.nextElementSibling.children[0].style.visibility = "visible";
            }, 500);
            i.nextElementSibling.style.height = "auto";
            i.nextElementSibling.children[0].classList.add('visible');
            i.nextElementSibling.style.transform = "scaleY(1)";
            i.nextElementSibling.classList.add('show');
            i.children[1].style.transform = "rotateZ(220deg)";
            i.children[1].style.transition = "transform .5s ease-in";
        }
    }
});
