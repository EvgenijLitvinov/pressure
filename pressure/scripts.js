function openDel(data) {
    document.getElementById("myDel").style.display = "block";
    document.getElementById("delBut").setAttribute("name", "del");
    document.getElementById("delBut").setAttribute("value", data);
}

function closeDel() {
    document.getElementById("myDel").style.display = "none";
}

const myModal = document.getElementById('popup')
const myInput = document.getElementById('myInput')
myModal.addEventListener('shown.bs.modal', () => {
    myInput.focus()
})