const currentUser = JSON.parse(localStorage.getItem("currentUser"));

function checkAnswer() {
    let score = 0;

    const correctAnswers = {
        "34": "34",
        "Triangle": "Triangle",
        "36": "36", 
        "40 ": "40",
        "5 ": "5"
    };

    for (let questionName in correctAnswers) {
        const selected = document.querySelector(`input[name="${questionName}"]:checked`);
        console.log(selected);
        if (selected && selected.value === correctAnswers[questionName]) {
            score++;
        }
    }

    document.getElementById("h2").innerHTML=` You scored ${score} out of 5!`;
    const quizResult = {
        email: currentUser.email,
        score: score,
        total: 5
    };

    localStorage.setItem("quizResult", JSON.stringify(quizResult));
    console.log("Saved quiz result:", quizResult);
    window.location.href = "Home.html"; 

}
