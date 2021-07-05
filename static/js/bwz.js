const navSlide = () =>{
    const overlay = document.querySelector('.overlay');
    const overlayContent = document.querySelector('.overlay-content');
    const topnavWrapper = document.getElementById('myTopnavWrapper');
    const openClose = document.querySelector('.openclose');
    const navLinks = document.querySelectorAll('.overlay-content a');

    openClose.addEventListener('click', () => {
        //Toggle Nav
        // topnavWrapper.style.opacity = 0;

        //Animate Links
        // navLinks.forEach((link,index) => {
        //     if(link.style.animation) {
        //       link.style.animation = ''
        //     } else {
        //       link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
        //     }
        // });
    });



}
window.onscroll = function() {beSticky()};

var navbar = document.getElementById("myTopnavWrapper");

var sticky = navbar.offsetTop;
if (sticky == 0) {
  var navbar = document.getElementById("myTopnavWrapperMob");
  var sticky = navbar.offsetTop;
}

console.log(sticky);
function beSticky() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");

  } else {
    navbar.classList.remove("sticky");

  }

}


// function beResponsive() {
//   var x = document.getElementById("myTopnav");

//   var djangoView = "{{ request.resolver_match.url_name }}";
//   if (x.className === "topnav") {
// 	x.classList.add("responsive")
//   } else {
// 	x.classList.remove("responsive");
//   }
// }

function resizeWindow() {
  var w = window.outerWidth;
  var h = window.outerHeight;
  var txt = "Window size: width=" + w + ", height=" + h;
  var line = document.getElementById("post-cat-line");
  document.getElementById('post-cat-line').style.width = w-870 + 'px';
  // console.log(txt);
}

// function setActive () {
//   var header = document.getElementById("dropdown");
//   var btns = document.getElementsByClassName("dropbtn");
//   // btns[0].className += " active";
//   for (var i = 0; i < btns.length; i++) {
//     btns[i].addEventListener("click", function() {
//     // alert(this.className);
//     //this.classList.add("active");
//     var current = document.getElementsByClassName("dropbtn");
//     // alert(current.className);
//     // if ()
//     this.className += " active";
    
//     current[0].className = current[0].className.replace(" active", "");
//     });
//   }
// }

function openNav() {
    document.getElementById("BwzNav").style.animation = `navLinkFade 0.5s ease forwards 0.3s`;
  }

function closeNav() {
  document.getElementById("BwzNav").style.animation = `navLinkFade 0.5s ease backwards 0.3s`;
}

