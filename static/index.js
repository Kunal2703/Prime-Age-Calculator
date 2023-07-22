function calculateAge() {
    const form = document.getElementById("ageForm");
    const formData = new FormData(form);

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
