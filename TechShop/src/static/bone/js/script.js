$(document).ready(function() {
  $('#trigger').click(function() {
    $('#overlay').fadeIn(300);
    $("#overlay").css("z-index: -1;");
  });
  $('#close').click(function() {
    $('#overlay').fadeOut(300);
    $("#overlay").css("");

  });
});

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}


$('a.prev').click(function() {
	 prevSlide();
});
$('a.next').click(function() {
	 nextSlide();
});
$('.slideshow').click(function(){
	 nextSlide();
});

//initialize show
showSlide();

function prevSlide() {
	 $('.slideshow img:last').prependTo($('.slideshow'));
	 showSlide();
}

function nextSlide() {
	 $('.slideshow img:first').appendTo($('.slideshow'));
	 showSlide();
}

function showSlide(){
	 //hide (reset) all images
	 $('.slideshow img').hide();
	 //show first image
	 $('.slideshow img:first').fadeIn(500);
}
