"use strict";
//console.log("Heloo");

let x = document.getElementById("loginForm");
let y = document.getElementById("registerForm");
let z = document.getElementById("btn");

function regi() {
    x.style.left = "-400px";
    y.style.left = "50px";
    z.style.left = "110px";
}

function login() {
    x.style.left = "50px";
    y.style.left = "450px";
    z.style.left = "0px";
}

function validate(c) {
    document.getElementById("errorMsg").innerHTML = c;
    document.getElementById("flashMsg").style.display = "block";
}

x.addEventListener("submit", (e) => {
    console.log("Login submitted");

    let email = document.getElementById("userId");
    let pass = document.getElementById("loginpassword");
    let msg;

    if (!(/\S+@\S+\.\S+/.test(email.value) && email.value.length >= 5)) {
        msg = "Enter Proper Email ID!!!";
        validate(msg);
        e.preventDefault();
        //alert("Enter Proper Email ID!!!");
    } else if (pass.value.length <= 6) {
        msg = "Password Must be greater than 6 char";
        validate(msg);
        e.preventDefault();
        // alert("Password Must be greater than 6 char");
    } else if (pass.value.length >= 21) {
        msg = "Password Must be less than 20 char";
        validate(msg);
        e.preventDefault();
        //alert("Password Must be less than 20 char");
    }
});

y.addEventListener("submit", (e) => {
    console.log("REg submitted");
    //e.preventDefault();
    let emailID = document.getElementById("emailID");
    let registerpwd = document.getElementById("registerpwd");
    let reregisterpwd = document.getElementById("reregisterpwd");
    let msg;
    if (!(/\S+@\S+\.\S+/.test(emailID.value) && emailID.value.length >= 5)) {
        //alert("Enter Proper Email ID!!!");
        msg = "Enter Proper Email ID!!!";
        validate(msg);
        e.preventDefault();
    } else if (registerpwd.value.length <= 6 && reregisterpwd.value.length <= 6) {
        e.preventDefault();
        //alert("Password Must be greater than 6 char");
        msg = "Password Must be greater than 6 char";
        validate(msg);
    } else if (
        registerpwd.value.length >= 21 &&
        reregisterpwd.value.length >= 21
    ) {
        e.preventDefault();
        //alert("Password Must be less than 20 char");
        msg = "Password Must be less than 20 char";
        validate(msg);
    } else if (registerpwd.value != reregisterpwd.value) {
        //alert("Both passwords sholud be match");
        msg = "Both passwords sholud be match";
        validate(msg);
        e.preventDefault();
    }
});

document.getElementById("closeMsg").addEventListener("click", () => {
    document.getElementById("flashMsg").style.display = "none";
});
