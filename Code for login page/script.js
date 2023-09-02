document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById("login_form");

  form.addEventListener("submit", function(event) {
    event.preventDefault();

    const form_data = new FormData(form);
    const email = form_data.get('email');
    const password = form_data.get('password');
    const data_sent = {
      email: email,
      password: password
    };

    const requestOptions = {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data_sent)
    };

    fetch('/', requestOptions)
      .then(response => response.json())
      .then(data => {
        console.log(data.verified);
        if (data.verified === "yes") {
          console.log("Verified");
          document.getElementById("work").innerHTML = "Welcome to the protected page!";
        } else {
          console.log("Not Verified");
          document.getElementById("work").innerHTML = "Access denied. Please verify your credentials first.";
        }
      })
      .catch(error => {
        console.error('Error:', error.message);
        document.getElementById("work").innerHTML = "An error occurred. Please try again later.";
      });
  });
});