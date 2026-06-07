const submitBtn = document.getElementById("submitBtn");
const retryBtn = document.getElementById("retryBtn");

submitBtn.addEventListener("click", function () {

    let score = 0;

    const questions =
        document.querySelectorAll(".question-card");

    questions.forEach(question => {

        const selected =
            question.querySelector(
                "input[type='radio']:checked"
            );

        const options =
            question.querySelectorAll(
                "input[type='radio']"
            );

        options.forEach(option => {

            option.disabled = true;

            const label = option.parentElement;

            if (option.dataset.correct === "true") {
                label.classList.add("correct");
            }

            if (
                selected &&
                option.checked &&
                option.dataset.correct === "false"
            ) {
                label.classList.add("wrong");
            }

        });

        if (
            selected &&
            selected.dataset.correct === "true"
        ) {
            score++;
        }

    });

    document.getElementById("result").innerHTML = `
        <div class="result-card">
            <div class="score">
                ${score} / ${questions.length}
            </div>
            <h3>Your Quiz Result</h3>
        </div>
    `;

    submitBtn.disabled = true;
    retryBtn.style.display = "inline-block";

    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
    });

});

retryBtn.addEventListener("click", function () {

    document
        .querySelectorAll("input[type='radio']")
        .forEach(input => {

            input.checked = false;
            input.disabled = false;
        });

    document
        .querySelectorAll(".correct")
        .forEach(item => {
            item.classList.remove("correct");
        });

    document
        .querySelectorAll(".wrong")
        .forEach(item => {
            item.classList.remove("wrong");
        });

    document.getElementById("result").innerHTML = "";

    submitBtn.disabled = false;
    retryBtn.style.display = "none";

    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });

});