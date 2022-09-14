const characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", ",", "|", ":", ";", "<", ">", ".", "?",
"/"];
let buttonEl = document.getElementById("btn")
const inputElFirst = document.getElementById("generateOne-el")
const inputElSecond = document.getElementById("generateTwo-el")
let characterLength = 12
function generateRandomPassword() {
    let randomPass = []
    for (i = 0; i < 16; i++) {
        let randomChr = Math.floor(Math.random() * characters.length)
        randomPass.push(characters[randomChr])
    }
    inputElFirst.value = randomPass.join('')
    inputElSecond.value = randomPass.join('')
    
}

