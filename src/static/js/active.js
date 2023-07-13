  // Obtenemos el enlace activo basado en la URL actual
  var url = window.location.pathname;
  var filename = url.substring(url.lastIndexOf('/') + 1);

  // Obtenemos todos los enlaces del navbar
  var enlaces = document.querySelectorAll('.enlace a');

  // Iteramos sobre los enlaces y verificamos si coinciden con el nombre del archivo actual
  enlaces.forEach(function(enlace) {
    var href = enlace.getAttribute('href');
    var enlaceFilename = href.substring(href.lastIndexOf('/') + 1);
    
    // Si el nombre del archivo coincide, agregamos la clase "active" al enlace
    if (enlaceFilename === filename) {
      enlace.classList.add('active');
    }
  });