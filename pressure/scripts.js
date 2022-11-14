function openDel(data) {
    document.getElementById("myDel").style.display = "block";
    document.getElementById("delBut").setAttribute("name", "yes");
    document.getElementById("delBut").setAttribute("value", data);
}

function closeDel() {
    document.getElementById("myDel").style.display = "none";
}