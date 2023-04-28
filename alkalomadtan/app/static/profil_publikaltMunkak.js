// globális változók
// html collection
var munkak = document.getElementById("mindenMunka");
// minden munkát ami megjelenni a django által eltárolja
var mindenMunkak_Tomb = mindenMunkak();
console.log(mindenMunkak_Tomb);
// a jelentlegi munkát adja vissza egy object-ként
let mostaniMunka = munkaMutatoStatusz();
var lapozoIndex = 0;

// Minden munka az oldalon
function mindenMunkak() {
    // egy tömb ami eltárolja munkákat amit a mindenMunka id-jó div-ban van
    let mindenMunka_Id = [];
    for (let i = 0; i < munkak.children.length; i++) {
        munkak.children.item(i).id = i;
        // ez egy object-et add majd hozzá
        mindenMunka_Id.push({
            id: parseInt(i),
            node: munkak.children.item(i)
        });
    }
    return mindenMunka_Id;
}

// minden látható munkát töröl
function osszesMunkaTorlo() {
    try {
        let megjelenoMunkakSzama = munkak.childElementCount;
        console.log("Eltávolítandó munkák száma: ", megjelenoMunkakSzama)
        for (let i = megjelenoMunkakSzama - 1; i >= 0; i--) {
            // ez majd kitörli a munkak gyermek elemét amit elmentettünk a munkak tömbbe
            munkak.removeChild(munkak.children.item(i));
            console.log("Munka elem ", i, "eltávolítva");
        }
    }
    catch (ex) {
        console.log("!", ex);
    }

}

// státusz ellenőrző (melyik munka megjelenítve)
function munkaMutatoStatusz() {
    /*
    ez majd egy string-et ad majd vissza, ami az adott div-nek az id-ja.
    Azon a logkián alapulva hogy úgy is csak egy munka lesz majd megjelenítve, így csak egy child lesz munkak div-ben.
    A visszatérési értéke egy szótár (dict) lesz
    */
    return { key: parseInt(munkak.children[0].id), value: munkak.children[0] };
}

// első megjelenítendő munkát ad vissza
/*
    úgytűnik ez a függvény a leges legutóbbi munkát mutatja
*/
function elsoMunka(munkakTomb) {
    munkak.appendChild(munkakTomb[0].node);
}
/*
    az alábbi függvények lesznek amik a nyilakat vezérlik a megjelenítendő munkákat
*/
// előre nyíl (jobbra mutató)
function eloreNyil(munkakTomb) {
    // evvel tudom hogy mi a most megjelenített munka
    console.log("lapozoIndex: ", lapozoIndex);
    try {
        if (lapozoIndex > munkakTomb.length || lapozoIndex === munkakTomb.length) {
            console.log("Nincs hová előre lapozni, így is túllépett! Vissza állítás a legutóbbi értékre!");
            lapozoIndex = munkakTomb.length - 1;
        } else {
            // hogyha a következő léséssal a munkakTomb hosszát érné el, akkor ne adjon hozzá új értéket{
            lapozoIndex++;
            console.log("lapozás elóre");
            console.log("Mostani oldal: ", munkakTomb[lapozoIndex]);
            const jelenlegiMunka = munkak.children.item(0);
            munkak.replaceChild(munkakTomb[lapozoIndex].node, jelenlegiMunka);
        }
    }
    catch {
        throw "Elfogyott a megjelenítendő oldal!";
    }
}
// hátra nyíl (balramutató)
function hatraNyil(munkakTomb) {
    // evvel tudom hogy mi a most megjelenített munka
    console.log("lapozás hátra");
    console.log("lapozoIndex: ", lapozoIndex);
    try {
        if (lapozoIndex < 0 || lapozoIndex === 0) {
            console.log("Nincs hová vissza lapozni!");
        } else if (lapozoIndex >= munkakTomb.length) {
            console.log("lapozás vissza");
            console.log("Túlnagy az index! Vissza lépés...")
            // addig csökkenti az éréket míg nem tudna visszalépni
            do {
                lapozoIndex--;
                console.log("lapozoIndex értéke: ", lapozoIndex)
            }
            while (lapozoIndex === munkakTomb.length)
            console.log("Mostani oldal: ", munkakTomb[lapozoIndex]);
            const jelenlegiMunka = munkak.children.item(0);
            munkak.replaceChild(munkakTomb[lapozoIndex].node, jelenlegiMunka)
        } else {
            lapozoIndex--;
            console.log("lapozás vissza");
            console.log("Mostani oldal: ", munkakTomb[lapozoIndex]);
            const jelenlegiMunka = munkak.children.item(0);
            munkak.replaceChild(munkakTomb[lapozoIndex].node, jelenlegiMunka)
        }
    }
    catch {
        throw "Elfogyott a megjelenítendő oldal!";
    }
}

// események
// előre lapozás
document.getElementById("lapozoElore").onclick = function () {
    eloreNyil(mindenMunkak_Tomb);
};

// hátra lapozás
document.getElementById("lapozoVissza").onclick = function () {
    hatraNyil(mindenMunkak_Tomb);
}

// függvény meghívások
document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    console.log("Event: ", event);

    osszesMunkaTorlo();
    elsoMunka(mindenMunkak_Tomb)
});
