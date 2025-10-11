// validacionRegistro.js
document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('.form-registro');
  const successMsg = document.getElementById('successMessage');

  form.addEventListener('submit', (e) => {
    e.preventDefault(); // Evita el envío real

    if (form.checkValidity()) {
      // Mostrar mensaje de éxito
      successMsg.style.display = 'block';
      successMsg.classList.add('show');

      // Limpiar campos
      form.reset();

      // Redirigir después de 2 segundos
      setTimeout(() => {
        window.location.href = './index.html';
      }, 2000);
    } else {
      // Mostrar mensajes nativos de error HTML5
      form.reportValidity();
    }
  });
});

