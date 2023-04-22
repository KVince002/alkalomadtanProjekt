// Minden munka az oldalon
function mindenMunkak() {
    // html collection
    var munkak = document.getElementById("mindenMunka");

    // egy tömb ami eltárolja munkákat amit a mindenMunka id-jó div-ban van
    let mindenMunka_Id = [];
    for (let i = 0; i < munkak.childElementCount; i++) {
        mindenMunka_Id.push(munkak.children.item(i));
        console.log("munka mentés tömbbe: ", i, " ez a ", mindenMunka_Id[i])
    }
    return mindenMunka_Id;
}

function osszesMunkaTorlo(munkakTomb) {
    var munkak = document.getElementById("mindenMunka");
    // ismeretlen hiba miatt biztosra megyek
    for (let i = 0; i < munkak.childElementCount + munkak.childElementCount; i++) {
        console.log("munka törlés: ", i, " ez a ", munkakTomb[i])
        munkak.removeChild(munkakTomb[i]);
    }
}

//függvény hívások
var mindenMunkak_Tomb = mindenMunkak();
osszesMunkaTorlo(mindenMunkak_Tomb);
