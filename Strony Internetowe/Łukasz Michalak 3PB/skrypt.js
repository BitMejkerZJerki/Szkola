let parzysta = prompt("Podaj liczbę:")
function liczbaparzysta(parzysta) {
    if (parzysta % 2 == 0){
        document.write("Liczba jest parzysta.")
    } else {
        document.write("Liczba nie jest parzysta.")
    }
}
liczbaparzysta(parzysta)

// zadanie II 

let a = prompt("Podaj liczbę a: ")
let b = prompt("Podaj liczbę b: ")
let c = prompt("Podaj liczbę c: ")


function delta(a,b,c) {
    let delta = b*b - 4*(a*c)
    document.write("<br></br>Delta = " + delta)
}

delta(a,b,c)

// zadanie III

let ciag1 = prompt("podaj ciąg 1: ")
let ciag2 = prompt("podaj ciąg 2: ")


function polaczenie(ciag1, ciag2){
    document.getElementById("but1")
    let polaczenie = ciag1 + ciag2
    document.write(polaczenie)
}

polaczenie(ciag1, ciag2)
