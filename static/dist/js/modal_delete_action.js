document.addEventListener('DOMContentLoaded', function() {
  var deleteModal = document.getElementById('deleteModal');
  
  deleteModal.addEventListener('show.bs.modal', function(event) {
      var button = event.relatedTarget; // Button that triggered the modal
      var actionUrl= button.getAttribute('data-url'); // Extract data-url
      
      var form = deleteModal.querySelector('#delete-form');
      form.setAttribute('action', actionUrl);
  });
});
