const formModal = document.getElementById('form-modal')
console.log(formModal)

const openModalBtn = document.getElementById('open-modal-btn')
const cancelBtn = document.getElementById('cancel-btn')

openModalBtn.addEventListener('click', ()=> {
    formModal.classlist.remove('aria-hidden')

})
cancelBtn.addEventListener('click', ()=> {
    formModal.classlist.add('aria-hidden')
})