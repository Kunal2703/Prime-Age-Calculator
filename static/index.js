function calculateAge() {
    const form = document.getElementById("ageForm");
    const birthYearInput = form.elements["birthYear"];
    const formData = new FormData(form);

    const yearPattern = /^[0-9]{4}$/;
    const errorMessage = document.getElementById("error-message");
    if (!yearPattern.test(birthYearInput.value)) {
        errorMessage.removeAttribute("hidden");
        return;
    } else {
        errorMessage.setAttribute("hidden", true);
    }

    fetch('/calculate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById("result");
        resultElement.textContent = `The next year when your age will be a prime number is: ${data.next_prime_year}`;
    });
}
