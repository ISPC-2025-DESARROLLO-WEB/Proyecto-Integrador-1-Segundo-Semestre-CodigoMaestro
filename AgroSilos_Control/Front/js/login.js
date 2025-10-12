document.getElementById('loginForm').addEventListener('submit', function(e) {
  e.preventDefault(); // Evita el envío automático del form

  // Usuario y contraseña fijos
  const usuarioValido = "admin";
  const contraseñaValida = "1234";

  // Lo que el usuario escribe
  const usuario = document.getElementById('usuario').value;
  const contraseña = document.getElementById('contraseña').value;

  const mensajeError = document.getElementById('mensajeError');

  if (usuario === usuarioValido && contraseña === contraseñaValida) {
    // lleva a la página principal
    window.location.href = "index.html"; 
  } else {
    mensajeError.textContent = "Usuario o contraseña incorrectos.";
  }
});