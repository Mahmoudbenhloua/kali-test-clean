function greetUser() {
  const name = document.getElementById("nameInput").value;
  fetch(`/api/greet?name=${encodeURIComponent(name)}`)
    .then(response => response.json())
    .then(data => {
      document.getElementById("output").innerText = data.greeting;
    });
}

function squareNumber() {
  const number = document.getElementById("numberInput").value;
  if (!number) {
    document.getElementById("output").innerText = "Please enter a number!";
    return;
  }

  fetch(`/api/square/${number}`)
    .then(response => response.json())
    .then(data => {
      document.getElementById("output").innerText = `Square of ${data.number} is ${data.squared}`;
    });
}
