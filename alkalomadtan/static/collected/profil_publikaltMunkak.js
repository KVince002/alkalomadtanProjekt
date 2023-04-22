// Minden munka az oldalon
function mindenMunkak()
{
    // html collection
    var munkak = document.getElementById("mindenMunka");

    // egy tömb ami eltárolja munkákat amit a mindenMunka id-jó div-ban van
    let mindenMunka_Id = [];
    for (let i = 0; i < munkak.children.length; i++){
        mindenMunka_Id.push(munkak.children.item(i));
    }

    return mindenMunka_Id;
}

function osszesMunkaTorlo(munkakTomb){
    var munkak = document.getElementById("mindenMunka");
    for (let i = 0; i < munkak.children.length; i++){
        munkak.removeChild(munkakTomb[i]);
    }
}

//függvény hívások
mindenMunkak()
osszesMunkaTorlo(mindenMunkak())
