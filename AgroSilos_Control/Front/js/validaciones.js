// Validación personalizada Bootstrap + envío simulado
document.getElementById('contactoForm').addEventListener('submit', function(e) {
  e.preventDefault(); // Evita el envío por defect
  
  const form = e.target;
  
  if (!form.checkValidity()) {
    e.stopPropagation(); // Detiene la propagación del evento.
    form.classList.add('was-validated'); //Agrega la clase de Bootstrap para mostrar errores
  } else {
    alert('✅ Mensaje enviado correctamente. ¡Gracias por contactarnos!');
    form.reset(); // Limpia el formulario
    form.classList.remove('was-validated'); // deja el formulario limpio visualmente
  }
});