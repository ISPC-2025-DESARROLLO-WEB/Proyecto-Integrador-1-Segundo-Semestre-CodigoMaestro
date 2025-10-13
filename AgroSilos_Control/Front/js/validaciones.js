// Validación personalizada Bootstrap + envío simulado
document.getElementById('contactoForm').addEventListener('submit', function(e) {
  const form = e.target;
  
  if (!form.checkValidity()) {
    e.preventDefault(); 
    e.stopPropagation();
    form.classList.add('was-validated');
  } else {
    // si todo está correcto, deja que FormSubmit procese el envío
    form.classList.add('was-validated');
  }
});