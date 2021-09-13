const w = window.outerWidth;
const navbar = document.getElementById("navbar");
const sticky = navbar.offsetTop;
const accordion = document.getElementsByClassName('accordion');
const breadcrumbs = document.getElementsByClassName('breadcrumbs');
const catWrapper = document.querySelector('.cat-wrapper');
var bc = document.getElementById('breadcrumbs');
if (category == 'FAQ'){
  catWrapper.classList.add('remove-background');
}
// Cookies-Consent
const cookieContainer = document.querySelector('.cookie-container');
const cookieButton = document.querySelector('.cookie-btn');
cookieButton.addEventListener('click',()=>{
  cookieContainer.classList.remove('active');
  localStorage.setItem('cookieBannerDisplayed', 'true')
});
setTimeout(() => {
  if (!localStorage.getItem('cookieBannerDisplayed')){
    cookieContainer.classList.add('active');
  }
}, 1000);


for (var i = 0, len = accordion.length; i < len; i++){
  accordion[i].addEventListener('click', function(){
    this.classList.toggle('active');
  })
};


if (w <= 769) {
  s.destroy();
  window.onscroll = function() {beSticky()};
  var bcWidth = 0;
  
  var maintext = document.getElementsByClassName('maintext');
  var documentImages = document.getElementsByTagName('img');
  var result = '';
  for (var i=0, len=documentImages.length|0; i<len; i=i+1|0) {
    result = documentImages[i].style.width;
    if (parseInt(result,10) >= 400){
      documentImages[i].style.width = '100%';
    }
  }
  
  

  function toggleX(x) {
    // console.log(sticky);
    x.classList.toggle("change");
    var navbar_ul = document.getElementById("navbar_ul");
    var bar1 = document.getElementById("bar1");
    var bar3 = document.getElementById("bar3");
    if (x.className == "menu-toggle change"){
      console.log('change yes');
      navbar_ul.style.display = 'flex';
      bar1.style.backgroundColor = "rgb(0, 170, 179)";
      bar3.style.backgroundColor = "rgb(0, 170, 179)";
      // navbar.classList.add("sticky");
      navbar_ul.style.zIndex = 10;
      navbar.style.zIndex = 10;
      
    } else {
      navbar_ul.style.display = 'none';
      bar1.style.backgroundColor = "white";
      bar3.style.backgroundColor = "white";
      
      beSticky();
    }  
  }
  document.onclick = function (e) {
    console.log(e.target.parentNode.offsetParent.className);
    const menuToggle = document.getElementById("menu-toggle");
    if (e.target.id !== 'navbar_ul' && e.target.id !== 'menu-toggle' && 
      e.target.id !== 'change' && e.target.id !== 'bar3' && e.target.id !== 'bar2' && e.target.id !== 'bar1' && 
      e.target.parentNode.offsetParent.className !== 'accordion')
    {
      menuToggle.classList.remove('change');
      navbar_ul.style.display = 'none';
      bar1.style.backgroundColor = "white";
      bar3.style.backgroundColor = "white";
      
    }
    if (!(e.target instanceof HTMLAnchorElement) && (e.target.id !== 'fname' && 
    e.target.id !== 'email' && e.target.id !== 'subject' && e.target.id !== 'message' && 
    e.target.id !== 'menu-toggle' && e.target.id !== 'bar3' && e.target.id !== 'bar2' && 
    e.target.id !== 'bar1' && e.target.parentNode.offsetParent.className !== 'accordion' && 
    e.target.parentNode.offsetParent.className !== 'accordion active' && window.pageYOffset > sticky))
    {
      navbar.style.position = 'fixed';
      navbar.style.top = 0;
      navbar.style.zIndex = 2;
    }
  }
  function beSticky() {
    if (window.pageYOffset >= sticky) {
      navbar.style.position = 'absolute';
      navbar.style.top = '100px';
    } 
  }
} else {
  window.onscroll = function() {beSticky()};
  
  var bcWidth = 0;
  var piWidth = 0;
  var factor = 0;
  var leftOffset = '';
  var refElement = [];
  if (djangoView == 'post_detail'){
    refElement = document.getElementsByClassName('post-intro');
    factor = 1;
  } else if (djangoView == 'category_view'){ 
    refElement = document.getElementsByClassName('gallery-cat');
    factor = 0.7;
  } else if (djangoView == 'contact_view'){ 
    refElement = document.getElementsByClassName('contact_container');
    factor = 1;
  } 
  else if (djangoView == 'about_view'){ 
    refElement = document.getElementsByClassName('about_container');
    factor = 1;
  } 
  
  for (var i = 0, len = breadcrumbs.length; i < len; i++) {
    bcWidth += breadcrumbs[i].offsetWidth;
  }
  for (var i = 0, len = refElement.length; i < len; i++) {
    piWidth += refElement[i].offsetWidth;
  }
  
  piWidth = piWidth * factor;
  
  if (djangoView == 'post_detail'){
    leftOffset = -(piWidth-bcWidth)+'px';
    bc.style.marginLeft = leftOffset;
    console.log(djangoView);
  } else if (djangoView == 'category_view'){ 
    leftOffset = (w-piWidth)/2+'px';
    console.log(bcWidth);
    console.log(piWidth);
    bc.style.marginLeft = leftOffset;
    catListCard1= document.getElementsByClassName('post-cat-card1');
    for (var i = 0, len = catListCard1.length; i < len; i++) {
      catListCard1[i].style.top = '12.5vw';
      catListCard1[i].style.top = '12.5vw';
    }
    catListCard2= document.getElementsByClassName('post-cat-card2');
    for (var i = 0, len = catListCard2.length; i < len; i++) {
      catListCard2[i].style.top = '12.5vw';
      catListCard2[i].style.top = '12.5vw';
    }
  }
  else if (djangoView == 'contact_view' || djangoView == 'about_view'){ 
    leftOffset = -(piWidth-bcWidth)+'px';
    console.log(bcWidth);
    console.log(piWidth);
    bc.style.marginLeft = leftOffset;
  }

  //ovdje je sve dobro. ne diraj
  function beSticky() {
    if (djangoView != 'home'){
      bc.style.zIndex = 0;
    }
    if (window.pageYOffset >= sticky) {
      console.log(sticky);
      navbar.style.position = 'fixed';
      navbar.style.top = 0;
    } else {
      navbar.style.position = 'absolute';
      navbar.style.top = '100px';
    }
  }
}