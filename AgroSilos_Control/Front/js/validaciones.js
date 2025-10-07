// Validación personalizada Bootstrap + envío simulado
document.getElementById('contactoForm').addEventListener('submit', function(e) {
  e.preventDefault(); // Evita el envío por defecto
  
  const form = e.target;
  
  if (!form.checkValidity()) {
    e.stopPropagation();
    form.classList.add('was-validated');
  } else {
    alert('✅ Mensaje enviado correctamente. ¡Gracias por contactarnos!');
    form.reset();
    form.classList.remove('was-validated');
  }
});