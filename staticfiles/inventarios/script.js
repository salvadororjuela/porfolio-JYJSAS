var Index = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("slide");
  var puntos = document.getElementsByClassName("punto");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  Index++;
  if (Index > slides.length) {Index = 1}    
  for (i = 0; i < puntos.length; i++) {
    puntos[i].className = puntos[i].className.replace(" active", "");
  }
  slides[Index-1].style.display = "block";  
  puntos[Index-1].className += " active";
  setTimeout(showSlides, 3000); // Cambia la imagen cada 3 segundos
}