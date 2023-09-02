//carousel-start

const track= document.querySelector(".carousel-track")
const slides= Array.from(track.children)
const next_btn= document.querySelector(".next"); 
const prev_btn= document.querySelector(".prev"); 

const dots_nav= document.querySelector(".carousel-nav")
const dots= Array.from(dots_nav.children)

const slide_width= slides[0].getBoundingClientRect().width;

// arranging the slides
const setSlidePos=(slide,index) => {
    slide.style.left= slide_width * index +"px";
}
slides.forEach(setSlidePos)


const moveToSlide = (track, currentSlide, targetSlide) =>{
    track.style.transform='translateX(-' + targetSlide.style.left + ')'
    currentSlide.classList.remove('currentSlide')
    targetSlide.classList.add('currentSlide')
}

const updateDots=(currentDot,targetDot)=>{
    currentDot.classList.remove('currentSlide')
    targetDot.classList.add('currentSlide')
}

const hideShowArrow= (slides,prev_btn,next_btn,targetIndex) =>{
    if (targetIndex === 0){
        prev_btn.classList.add('is-hidden')
        next_btn.classList.remove('is-hidden')
    }
    else if(targetIndex === slides.length-1){
        prev_btn.classList.remove('is-hidden')
        next_btn.classList.add('is-hidden')
    }
    else{
        prev_btn.classList.remove('is-hidden')
        next_btn.classList.remove('is-hidden')
    }
}


next_btn.addEventListener("click", e => {
    const currentSlide= track.querySelector(".currentSlide");
    const nextSlide= currentSlide.nextElementSibling;

    const currentDot= dots_nav.querySelector('.currentSlide')
    nextDot=currentDot.nextElementSibling;

    const nextIndex=slides.findIndex(slide => slide===nextSlide)

    moveToSlide(track,currentSlide,nextSlide);
    updateDots(currentDot,nextDot); 
    hideShowArrow(slides,prev_btn,next_btn,nextIndex);
})


prev_btn.addEventListener("click", e => {
    const currentSlide= track.querySelector(".currentSlide");
    const prevSlide= currentSlide.previousElementSibling;

    const currentDot= dots_nav.querySelector('.currentSlide')
    prevDot=currentDot.previousElementSibling;

    const prevIndex=slides.findIndex(slide => slide===prevSlide)
    

    moveToSlide(track,currentSlide,prevSlide)
    updateDots(currentDot,prevDot);
    hideShowArrow(slides,prev_btn,next_btn,prevIndex); 
})


// dots nav
dots_nav.addEventListener('click',e =>{
    const targetDot=e.target.closest('button');
    if(!targetDot) return;

    const currentSlide=track.querySelector('.currentSlide');
    const currentDot=dots_nav.querySelector('.currentSlide');
    const targetIndex= dots.findIndex(dot => dot === targetDot);
    const targetSlide = slides[targetIndex];

    moveToSlide(track,currentSlide,targetSlide)
    updateDots(currentDot,targetDot)
    hideShowArrow(slides,prev_btn,next_btn,targetIndex)
})
//carousel-end

//Chat gpt's----navlinks scrolling

const scrollLinks = document.querySelectorAll(".nav-links");

scrollLinks.forEach(link => {
    link.addEventListener("click", function(event) {
        event.preventDefault();

        const targetId = this.getAttribute("data-target");
        const targetSection = document.getElementById(targetId);

        if (targetSection) {
            const targetOffset = targetSection.getBoundingClientRect().top;
            const startPosition = window.pageYOffset;
            const duration = 1000; // Adjust the duration (in milliseconds) as needed
            let startTime;

            function scrollAnimation(currentTime) {
                if (!startTime) startTime = currentTime;
                const progress = currentTime - startTime;
                const scrollY = easeInOutQuad(progress, startPosition, targetOffset, duration);
                window.scrollTo(0, scrollY);

                if (progress < duration) {
                    requestAnimationFrame(scrollAnimation);
                }
            }

            function easeInOutQuad(t, b, c, d) {
                t /= d / 2;
                if (t < 1) return (c / 2) * t * t + b;
                t--;
                return (-c / 2) * (t * (t - 2) - 1) + b;
            }

            requestAnimationFrame(scrollAnimation);
        }
    });
});

//navlinks-end

//rooms-section
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
