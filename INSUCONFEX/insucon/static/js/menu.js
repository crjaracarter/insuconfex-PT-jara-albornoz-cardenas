// Obtener el elemento del botón del menú hamburguesa
var menuButton = document.getElementById('menu-button');

// Obtener el elemento del menú móvil
var mobileMenu = document.getElementById('mobile-menu');

// Agregar un evento de clic al botón del menú hamburguesa
menuButton.addEventListener('click', function() {
  // Alternar la clase 'active' en el menú móvil
  mobileMenu.classList.toggle('active');

  // Agregar o eliminar la clase 'right' en función del estado del menú móvil
  if (mobileMenu.classList.contains('active')) {
    mobileMenu.classList.add('right');
  } else {
    mobileMenu.classList.remove('right');
  }
});

