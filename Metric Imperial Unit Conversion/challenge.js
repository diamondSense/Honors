let btnEl = document.getElementById("btn-el")
let inputEl = document.getElementById("input-el")
let lengthEl = document.getElementById("length-el")
let volumeEl = document.getElementById("volume-el")
let massEl = document.getElementById("mass-el")
let refreshEl = document.getElementById("refresh-el")

const meterToFeet = 3.281
const literToGallon = 0.264 
const kilogramToPound = 2.204

btnEl.addEventListener("click", function(){
    let baseValue = inputEl.value
    lengthEl.textContent = `${baseValue} meter = ${baseValue * meterToFeet} feet`
    volumeEl.textContent = `${baseValue} liters = ${baseValue * literToGallon} gallon`
    massEl.textContent = `${baseValue} kilogram = ${baseValue * kilogramToPound} pound`
})
function reload(){
    window.location.reload()
}
