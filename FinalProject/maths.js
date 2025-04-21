function checkAnswer() {
    let score = 0;

    // Correct answers:
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

    document.getElementById("h2").innerHTML=`🌟 You scored ${score} out of 5!`;
}
