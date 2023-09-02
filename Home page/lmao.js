// JavaScript to handle room selection
const selectButtons = document.querySelectorAll(".room-btn");
let selectedRoom = null;

selectButtons.forEach(function (button) {
    button.addEventListener("click", function () {
        const roomType = this.getAttribute("data-room");

        // Check if the button is already selected
        const isAlreadySelected = this.classList.contains("selected-button");

        // Deselect the button if it's already selected
        if (isAlreadySelected) {
            this.classList.remove("selected-button");
            selectedRoom = null;
        } else {
            // Deselect any previously selected button
            const previouslySelectedButton = document.querySelector(".room-btn.selected-button");
            if (previouslySelectedButton) {
                previouslySelectedButton.classList.remove("selected-button");
            }

            // Select the clicked button
            this.classList.add("selected-button");
            selectedRoom = roomType;
        }
    });
});


// JavaScript for "Read More" button
const toggleButtons = document.querySelectorAll(".toggle-amenities-btn");

toggleButtons.forEach(function (button) {
    button.addEventListener("click", function () {
        const amenitiesList = this.parentNode.querySelector(".amenities-list");
        if (amenitiesList) {
            const amenityItems = amenitiesList.querySelectorAll(".amenity-item");
            amenityItems.forEach(function (item, index) {
                if (index >= 5) {
                    item.classList.toggle("hidden");
                }
            });
            const buttonText = this.textContent;
            this.textContent = buttonText === "Read More" ? "Read Less" : "Read More";
        }
    });
});

// JavaScript function to handle form submission
function submitForm(event) {
    event.preventDefault(); // Prevent the form from submitting traditionally

    // Get user input from the form
    const customerName = document.getElementById("customerName").value;
    const numberOfPeople = document.getElementById("numberOfPeople").value;
    const customerPhoneNumber = document.getElementById("customerPhoneNumber").value;
    const customerEmail = document.getElementById("customerEmail").value;
    emailPattern=/^[a-zA-Z0-9._-]+@gmail\.com$/

    // Check if a room is selected
    if (selectedRoom) {
        // Create a JSON dictionary (object) with the collected data
        if(customerPhoneNumber.length===10){
            if(emailPattern.test(customerEmail)){
                const userData = {
                    "Name": customerName,
                    "Number of People": numberOfPeople,
                    "Phone Number": customerPhoneNumber,
                    "Email": customerEmail,
                    "Selected Room Type": selectedRoom
                };
                const userDataJSON = JSON.stringify(userData);
                // Display the JSON data (you can replace this with your preferred method)
                alert("User Data (JSON):\n" + userDataJSON);
        
                // Convert the JSON object to a JSON string for easy transmission or storage
                
            }
            else{
                alert("invalid email id")
            }
        }
        else{
            alert("invalid phone number")
        }
        

        // You can also reset the form after submission if needed
        // document.getElementById("userInfoForm").reset();
    } else {
        // Handle the case where no room is selected
        alert("Please select a room before submitting.");
    }
}
