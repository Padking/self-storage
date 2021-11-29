var myModal = document.getElementById('boxRentModal')
var myInput = document.getElementById('exampleInputEmail1')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})
