document.addEventListener("DOMContentLoaded", ()=> {
    var signupForm = document.getElementById("signup-form");
    var signupButton = document.getElementById("signup-button");
    var firstname = document.getElementById("first-name");
    var lastname = document.getElementById("last-name");
    var username = document.getElementById("username");
    var email = document.getElementById("email");
    var password = document.getElementById("password");
    var usernameError = document.getElementById("username-error");
    var emailError = document.getElementById("email-Error");
   
    // function to toggle the  signup the signup button state
    var togglesignupButton = () => {
        if (checkValidation()) {
            signupButton.removeAttribute("disabled");
        } else {
            signupButton.removeAttribute("disabled", "disabled");
        }
    };


    // function to validate the email format 

    var isValidEmail = () => {
        const emailRegex = /^[a-zA-Z0-9,_%+-]+@[a-za-Z0-9,-]+\,[a-zA-Z]{2,}$/;
        if(emailRegex.test(emailInput.value)) {
            emailError.textContent ="valid Email";
            emailError.style.color = "green";
            emailError.style.display = "block";
            return true;
        } else {
            emailError.textContent = "Invalid Email";
            emailError.style.color = "red";
            emailError.style.display = " block";
            return false;
        }
    };

    // function to check email availability
    var isemailAvailable = () => {
        return new Promise((resolve,reject)  => {
            var xhr =new XMLHttpRequest();
            xhr.onreadystatechange = function () {
                if(xhr.readyState === XMLHttpRequest.DONE) {
                  if(xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    if(response.available) {
                        emailError.textContent = "Email is available";
                        emailError.style.color = "green";
                        emailError.style.display = "block";
                        resolve (true);
                    } else {
                        emailError.textContent = "Email is available";
                        emailError.style.color = "red";
                        emailError.style.display = "block";
                        resolve(false);
                    } 
                  } else {
                    reject(xhr.status);
                  }
                }
            };
            xhr.open("GET", "/check-email/?email=" + encodeURIComponent(emailInput.value),true);
            xhr.send();
        });
    };

    // Function to validte the username format 
    var isValidUsername = () => {
        const usernameRegex = /^[a-zA-Z0-9_3]{3,}$/;
        if (usernameRegex.test(usernameInput.value)) {
            usernameError.textContent = "Valid Username";
            usernameError.style.color = "green";
            usernameError.style.display = "block";
            return true;
        } else {
            usernameError.textContent = "Invalid Username";
            usernameError.style.color = "green";
            usernameError.style.display = "block";
            return false;
        }
    }
    
    // function to check username avaialability
    var isValidusernameAvailable = () => {
        return new Promise((resolve,reject) => {
            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                if(xhr.status === XMLHttpRequest.DONE) {
                    if(xhr.status === 200) {
                        var response = JSON.parse(xhr.responseText);
                        if (response.available) {
                            usernameError.textContent = "Username is available";
                            usernameError.style.color = "grren";
                            usernameError.style.display = "block";
                            resolve(true);
                        } else {
                            usernameError.textContent = "Username is not available";
                            usernameError.style.color = "grren";
                            usernameError.style.display = "block";
                            resolve(false);
                        }
                    } else {
                        reject(xhr.status);
                    }
                }
            };
            xhr.open("GET","/check-username/?username=" + encodeURIComponent(usernameInput), true);
            xhr.send();
        });
    };

    // function to check if all fields are filled and valid
    var checkValidation = () => {
        return (
            firstname.value !== "" &&
            lastname.value !== "" &&
            username.value !== "" &&
            isValidUsername() &&
            email.value !== "" &&
            isValidEmail() &&
            password.value !== "" 
        );
    };

    // Event listner for form inputs

    signupForm.addEventListener("input", () => {
        togglesignupButton();
    });

    // Event listner for form subbmission
    signupForm.addEventListener("submit", (Event) => {
        Event.preventDefault(); // prevent form subbmission

        if (checkValidation()) {
            // perform user and email availability checks
            Promise.all([isemailAvailable(),isValidusernameAvailable()])
            .then((results) => {
                // if both email and username are availabel, submit the form
                if (results.every((result) => result == true)) {
                    signupForm.submit();
                }
            })
            .catch((error) => {
                console.error("Error",error);
            });
        }
    });
});