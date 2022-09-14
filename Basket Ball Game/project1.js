let homeScoreBtnOne = document.getElementById("home-score-btn-1")
let homeScoreBtnTwo = document.getElementById("home-score-btn-2")
let homeScoreBtnThree = document.getElementById("home-score-btn-3")
let homeScoreEl =document.getElementById("home-score")
let homeScore = 0

function increaseHomeScoreOne(){
    homeScore += 1
    homeScoreEl.textContent = homeScore
}
function increaseHomeScoreTwo(){
    homeScore += 2
    homeScoreEl.textContent = homeScore
}
function increaseHomeScoreThree(){
    homeScore += 3
    homeScoreEl.textContent = homeScore
}  
let awayScoreBtnOne = document.getElementById("away-score-btn-1")
let awayScoreBtnTwo = document.getElementById("away-score-btn-2")
let awayScoreBtnThree = document.getElementById("away-score-btn-3")
let awayScoreEl =document.getElementById("away-score")
let awayScore = 0

function increaseAwayScoreOne(){
    awayScore += 1
    awayScoreEl.textContent = awayScore
}
function increaseAwayScoreTwo(){
    awayScore += 2
    awayScoreEl.textContent = awayScore
}
function increaseAwayScoreThree(){
    awayScore += 3
    awayScoreEl.textContent = awayScore
}  