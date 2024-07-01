/* Home.js por Ceress79*/

function toggleMenu_general() {
    const menuCuadro = document.getElementById('menu-cuadro');
    menuCuadro.classList.toggle('visible');
}

function toggleMenuNotificaciones() {
    const menuNotificaciones = document.getElementById('menu-notificaciones');
    const fondoOscuro = document.getElementById('fondo-oscuro');
    
    const isVisible = menuNotificaciones.style.display === 'block';
    
    if (isVisible) {
        menuNotificaciones.style.display = 'none';
        fondoOscuro.style.display = 'none';
    } else {
        menuNotificaciones.style.display = 'block';
        fondoOscuro.style.display = 'block';
    }
}

// Para ocultar el menú de notificaciones al hacer clic en el fondo oscuro
document.getElementById('fondo-oscuro').addEventListener('click', function() {
    document.getElementById('menu-notificaciones').style.display = 'none';
    this.style.display = 'none';
});

document.addEventListener('DOMContentLoaded', function () {
    const rectangulo_loops = document.getElementById('rectangulo_loops');
    const boton_navegacion_loops = document.getElementById('boton_navegacion-loops');
    const desplejable3_src = document.getElementById('desplejable3-src');

    const expandSrc = boton_navegacion_loops.getAttribute('desplejable1-src');
    const collapseSrc = boton_navegacion_loops.getAttribute('desplejable2-src');

    boton_navegacion_loops.addEventListener('click', function () {
        if (rectangulo_loops.classList.contains('desplejar-loops')) {
            rectangulo_loops.classList.remove('desplejar-loops');
            desplejable3_src.src = collapseSrc;
        } else {
            rectangulo_loops.classList.add('desplejar-loops');
            desplejable3_src.src = expandSrc;
        }
    });
});
