const currentUser = JSON.parse(localStorage.getItem("currentUser"));
console.log("Current User Object:", currentUser);
function checkAnswerBio() {
    let score = 0;

    if (!currentUser) {
        alert("You must be logged in to take the quiz!");
        window.location.href = "FinalProject.html"; 
    }

    const correctAnswers = {
        "Oxygen": "Oxygen",
        "Nucleus": "Nucleus",
        "Plasma": "Plasma", 
        "Saturn ": "Saturn",
        "Gravity": "Gravity"
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
