// globális változók
// html collection
var munkak = document.getElementById("mindenMunka");

// Minden munka az oldalon
function mindenMunkak() {
    // egy tömb ami eltárolja munkákat amit a mindenMunka id-jó div-ban van
    let mindenMunka_Id = [];
    for (let i = 0; i < munkak.children.length; i++) {
        munkak.children.item(i).id = i;
        mindenMunka_Id.push(munkak.children.item(i));
        console.log("munka mentés tömbbe: ", i, " ez a ", mindenMunka_Id[i])
    }
    return mindenMunka_Id;
}

// minden látható munkát töröl
function osszesMunkaTorlo(munkakTomb) {
    // ismeretlen hiba miatt biztosra megyek
    for (let i = 0; i < munkakTomb.length; i++) {
        console.log("munka törlés: ", i, " ez a ", munkakTomb[i])
        munkak.removeChild(munkakTomb[i]);

    }
}

// státusz ellenőrző (melyik munka megjelenítve)
function munkaMutatoStatusz() {
    /*
    ez majd egy string-et ad majd vissza, ami az adott div-nek az id-ja.
    Azon a logkián alapulva hogy úgy is csak egy munka lesz majd megjelenítve, így csak egy child lesz munkak div-ben
    */
    return munkak.children[0].id
}

// első megjelenítendő munkát ad vissza
/*
    úgytűnik ez a függvén a leges legutóbbi munkát mutatja
*/
function elsoMunka(munkakTomb) {
    munkak.appendChild(munkakTomb[0]);
}

/*
    az alábbi függvények lesznek amik a nyilakat vezérlik a megjelenítendő munkákat
*/
// előre nyíl (jobbra mutató)
function eloreNyil(munkakTomb) {
    let mostaniMunka = munkaMutatoStatusz();

}

// függvény meghívások
window.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    //függvény hívások
    var mindenMunkak_Tomb = mindenMunkak();
    osszesMunkaTorlo(mindenMunkak_Tomb);

    elsoMunka(mindenMunkak_Tomb)
});