// validacionRegistro.js
document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('.form-registro');
  const successMsg = document.getElementById('successMessage');
  const password = document.getElementById('password');
  const confirmPassword = document.getElementById('confirmPassword');

  // Crear mensaje de error para contraseñas diferentes
  let errorMsg = document.createElement('p');
  errorMsg.id = 'passwordError';
  errorMsg.style.color = 'red';
  errorMsg.style.display = 'none';
  confirmPassword.parentNode.insertBefore(errorMsg, confirmPassword.nextSibling);

  // Validación en tiempo real
  confirmPassword.addEventListener('input', () => {
    if (confirmPassword.value && password.value !== confirmPassword.value) {
      errorMsg.textContent = 'Las contraseñas no coinciden.';
      errorMsg.style.display = 'block';
      confirmPassword.setCustomValidity('Las contraseñas no coinciden.');
    } else {
      errorMsg.textContent = '';
      errorMsg.style.display = 'none';
      confirmPassword.setCustomValidity('');
    }
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault(); 

    // Validar contraseñas antes de continuar
    if (password.value !== confirmPassword.value) {
      errorMsg.textContent = 'Las contraseñas no coinciden.';
      errorMsg.style.display = 'block';
      confirmPassword.setCustomValidity('Las contraseñas no coinciden.');
      form.reportValidity();
      return;
    } else {
      errorMsg.textContent = '';
      errorMsg.style.display = 'none';
      confirmPassword.setCustomValidity('');
    }

    if (form.checkValidity()) {
      // Mostrar mensaje de éxito
      successMsg.style.display = 'block';
      successMsg.classList.add('show');

      // Limpiar campos
      form.reset();

      setTimeout(() => {
        window.location.href = './index.html';
      }, 2000);
    } else {

      form.reportValidity();
    }
  });
});

