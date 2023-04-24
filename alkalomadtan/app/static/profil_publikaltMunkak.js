// globális változók
// html collection
var munkak = document.getElementById("mindenMunka");
// minden munkát ami megjelenni a django által eltárolja
var mindenMunkak_Tomb = mindenMunkak();
// a jelentlegi munkát adja vissza egy object-ként
let mostaniMunka = munkaMutatoStatusz();

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
    try {
        console.log(munkak.childElementCount)
        for (let i = 0; i < munkak.childElementCount; i++) {
            console.log("munka törlés: ", i, " ez a ", munkakTomb[i])
            munkak.removeChild(munkakTomb[i]);

        }
    }
    catch (ex) {
        console.log("!")
        console.log(ex);
    }

}

// státusz ellenőrző (melyik munka megjelenítve)
function munkaMutatoStatusz() {
    /*
    ez majd egy string-et ad majd vissza, ami az adott div-nek az id-ja.
    Azon a logkián alapulva hogy úgy is csak egy munka lesz majd megjelenítve, így csak egy child lesz munkak div-ben.
    A visszatérési értéke egy szótár (dict) lesz
    */
    return { key: munkak.children[0].id, value: munkak.children[0] };
}

// első megjelenítendő munkát ad vissza
/*
    úgytűnik ez a függvény a leges legutóbbi munkát mutatja
*/
function elsoMunka(munkakTomb) {
    munkak.appendChild(munkakTomb[0]);
}
/*
    az alábbi függvények lesznek amik a nyilakat vezérlik a megjelenítendő munkákat
*/
// előre nyíl (jobbra mutató)
function eloreNyil(munkakTomb) {
    // evvel tudom hogy mi a most megjelenített munka
    console.log("lapozás előre");
    if (munkakTomb.length > 1) {
        // törölje a most megjelenő munkát
        munkak.removeChild(mostaniMunka.value);
    }
}

// gombok
document.getElementById("lapozoElore").onclick = eloreNyil(mindenMunkak_Tomb);

// függvény meghívások
// document.addEventListener("DOMContentLoaded", (event) => {
//     console.log("DOM fully loaded and parsed");

// });

//függvény hívások
osszesMunkaTorlo(mindenMunkak_Tomb);
elsoMunka(mindenMunkak_Tomb)