const header = document.getElementById('header');
const search_bar = document.getElementById('searchbar').childNodes[1];
const titles = document.querySelectorAll('.detail .title');
const scrollToTop = document.getElementById('scroll-top');
const searchButton = document.getElementById('search-btn');


search_bar.addEventListener('keypress', (event) =>{
  if(event.key === 'Enter'){
  let targetId = "";
    let input_res = (search_bar.value);
    for (let i = 0; i < titles.length; i++) {
      let index = titles[i].childNodes[1].innerHTML.indexOf(input_res);
      if (index !== -1) {
        targetId = titles[i];
        console.log(targetId)
        titles[i].scrollIntoView();
        break;
      }
    }
  }
});

function findString(text) {
  let targetId = "";
  let inputRes = text;
  for (let i = 0; i < titles.length; i++) {
    let index = titles[i].childNodes[1].innerHTML.indexOf(inputRes);
    if (index !== -1) {
      targetId = titles[i];
      console.log(targetId)
      titles[i].scrollIntoView();
      break;
    }
  }
};
scrollToTop.addEventListener('click', () =>{
  window.scrollTo({top: 0, left: 0, behavior:"smooth"});
});

searchButton.addEventListener('click', () =>{
  let targetId = "";
  let input_res = (search_bar.value);
    for (let i = 0; i < titles.length; i++) {

      let index = titles[i].childNodes[1].innerHTML.indexOf(input_res);
      if (index !== -1) {
        targetId = titles[i];
        titles[i].style.backgroundcolor = '#2fabea';
        titles[i].scrollIntoView();
        break;
      }
    }
});

// if (window.innerWidth <= 1024){
//     let searchPosition = ruleSearchBar.offsetTop
//     document.onscroll = () => {
//       console.log(searchPosition)
//
//     }
//
// }else{
//         ruleSearchBar.style.position = 'inline';
// }