// Función para abrir el modal de cambio de imagen de banner
function openBannerModal() {
    document.getElementById("bannerModal").style.display = "block";
}

// Función para cerrar el modal de cambio de imagen de banner
function closeBannerModal() {
    document.getElementById("bannerModal").style.display = "none";
}

function openProfileModal() {
    document.getElementById("profileModal").style.display = "block";
}

function closeProfileModal() {
    document.getElementById("profileModal").style.display = "none";
}


// Función para subir la imagen del banner
function uploadBannerImage() {
    var input = document.getElementById("bannerInput");
    var file = input.files[0];

    if (file) {
        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById("bannerImage").style.backgroundImage = "url('" + e.target.result + "')";
        }
        reader.readAsDataURL(file);
        closeBannerModal(); // Cierra el modal después de cargar la imagen
    }
}

function uploadProfileImage() {
    var input = document.getElementById("profileInput");
    var file = input.files[0];

    if (file) {
        var reader = new FileReader();
        reader.onload = function(e) {
            document.querySelector('.profile-picture img').src = e.target.result;
        }
        reader.readAsDataURL(file);
        closeProfileModal();
    }
}


// Código JavaScript para el perfil
console.log('Perfil cargado');
