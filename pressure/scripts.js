function openDel(data) {
    document.getElementById("myDel").style.display = "block";
    document.getElementById("delBut").setAttribute("name", "del");
    document.getElementById("delBut").setAttribute("value", data);
}

function closeDel() {
    document.getElementById("myDel").style.display = "none";
}
/*
window.onscroll = function() {
    if (window.scrollY <= window.innerHeight /4) {
        location.reload();
    }
}
*/
const myModal = document.getElementById('popup')
const myInput = document.getElementById('myInput')
myModal.addEventListener('shown.bs.modal', () => {
    myInput.focus()
})

function more10() {
    let params = (new URL(document.location)).searchParams;
    params.set("more", "1");
    location.reload();
}