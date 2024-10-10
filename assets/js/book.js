const header = document.getElementById('header');
const search_bar = document.getElementById('searchbar').childNodes[1].childNodes[1];
const titles = document.querySelectorAll('.detail .title');
const scrollToTop = document.getElementById('scroll-top');
const searchButton = document.getElementById('search-btn');

search_bar.addEventListener('keypress', (event) =>{
  if(event.key === 'Enter'){
    console.log(search_bar)
  let targetId = "";
    let input_res = (search_bar.value);
    for (let i = 0; i < titles.length; i++) {
      let index = titles[i].childNodes[1].innerHTML.indexOf(input_res);
      if (index !== -1) {
        targetId = titles[i];
        titles[i].scrollIntoView({block: 'center'});
        break;
      }
    }
  }
});

function findString(text) {
  let targetId = "";
  // let inputRes = text;
  for (let i = 0; i < titles.length; i++) {
    let index = titles[i].childNodes[1].innerHTML.indexOf(text);
    if (index !== -1) {
      targetId = titles[i];
      titles[i].scrollIntoView({block: 'center'});
      break;
    }
  }
}

scrollToTop.addEventListener('click', () =>{
  window.scrollTo({top: 0, left: 0, behavior:"smooth"});
});
console.log(search_bar)
searchButton.addEventListener('click', () =>{
  let targetId = "";
  let input_res = (search_bar.value);
    for (let i = 0; i < titles.length; i++) {

      let index = titles[i].childNodes[1].innerHTML.indexOf(input_res);
      if (index !== -1) {
        targetId = titles[i];
        titles[i].scrollIntoView({block: 'center'});
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