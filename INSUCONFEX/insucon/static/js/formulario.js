const formulario_cli = document.getElementById('formulario_cli');
const inputs = document.querySelectorAll('#formulario_cli input');

const expresiones = {
	idCliente: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombreCliente: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/,
    comuna: /^[a-zA-ZÀ-ÿ\s]{1,40}$/,
    direccion: /^[a-zA-ZÀ-ÿ\s]{1,40}$/,   
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{9}$/ // 8 a 9 numeros.
}

