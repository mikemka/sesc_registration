for (let i = 1; i <= 11; i++) {
    document.getElementById(`id_d${i}`).onclick = function () {
        let d1 = Number(document.getElementById('id_d1').checked) * 2;
        let d2 = Number(document.getElementById('id_d2').checked);
        let d3 = Number(document.getElementById('id_d3').checked);
        let d4 = Number(document.getElementById('id_d4').checked);
        let d5 = Number(document.getElementById('id_d5').checked);
        let d6 = Number(document.getElementById('id_d6').checked);
        let d7 = Number(document.getElementById('id_d7').checked) * 2;
        let d8 = Number(document.getElementById('id_d8').checked) * 2;
        let d9 = Number(document.getElementById('id_d9').checked);
        let d10 = Number(document.getElementById('id_d10').checked) * 2;
        let d11 = Number(document.getElementById('id_d11').checked);
        let ext = d1 + d2 + d3 + d4 + d5 + d6 + d7 + + d8 + d9 + d10 + 28 + 3;
        document.getElementById("ext1").textContent = ext + d11;
        document.getElementById("ext2").textContent = ext + 1;
        document.getElementById("ext3").textContent = (ext + ext + 1 + d11) * 35;
        if ((ext < 31) || (ext + 1 > 37)) {
            document.getElementById("ext").className = "table-dark lead";
            document.getElementById("sbm-btn").className = "btn btn-primary disabled";
            document.getElementById("ext-info").textContent = "Неверное количество часов нагрузки";
        } else {
            document.getElementById("ext").className = "table-primary lead";
            document.getElementById("sbm-btn").className = "btn btn-primary";
            document.getElementById("ext-info").textContent = "Текущая недельная нагрузка";
        }
    }
}