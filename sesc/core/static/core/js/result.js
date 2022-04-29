let i = 1;
while (true) {
    let elem = document.getElementById(`d${i}_res`);
    if (elem != undefined) {
        elem.textContent = document.getElementById(`d${i}`).textContent * 70;
    } else {
        break;
    } 
    i++;
}