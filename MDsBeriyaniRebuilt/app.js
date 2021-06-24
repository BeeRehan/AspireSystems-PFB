const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const app = express();

app.use(bodyParser.json());
app.use(express.static("templates"));
app.use(
    bodyParser.urlencoded({
        extended: true,
    })
);

mongoose.connect("mongodb://localhost:3032/mydb", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on("error", () => console.log("Error in Connecting to Database"));
db.once("open", () => console.log("Connected to Database"));

app
    .get("/", (req, res) => {
        res.set({
            "Allow-access-Allow-Orgin": "*",
        });
        return res.redirect("Register.html");
    })
    .listen(3031);

app.post("/registration", (req, res) => {
    let emailId = req.body.emailID;
    console.log(emailId);
    let password = req.body.password;
    let repassword = req.body.repassword;
    let district = req.body.district;

    let data = {
        emailId,
        password,
        repassword,
        district,
    };

    db.collection("users").findOne({ emailId: emailId }, (err, docs) => {
        console.log(docs);
        if (docs == null) {
            db.collection("users").insertOne(data, (ierr, collection) => {
                if (ierr) {
                    throw ierr;
                }
                console.log("Record Inserted Successfully");
            });
        } else docs != null;
        console.log("Already Registered");
    });
    // db.collection("users").insertOne(data, (ierr, collection) => {
    //     if (ierr) {
    //         throw ierr;
    //     }
    //     console.log("Record Inserted Successfully");
    // });
    return res.redirect("Register.html");
});

app.post("/login", (req, res) => {
    let emailId = req.body.emailID;
    let password = req.body.password;
    db.collection("users").findOne({ emailId: emailId }, (ferr, docs) => {
        if (ferr) {
            throw ferr;
        }
        console.log(emailId, docs.emailId);
        if (emailId == docs.emailId && password == docs.password) {
            console.log("Welcome!!!");
            return res.redirect("base.html");
        } else {
            res.send(
                'Wrong Credential<br/><a href="Register.html " > Retutn LoginPage </a>'
            );
        }
    });
});

app.post("/quries", (req, res) => {
    let fisrtName = req.body.firstName;
    let LastName = req.body.lasttName;
    let email = req.body.EmailID;
    let message = req.body.message;

    const data = {
        fisrtName,
        LastName,
        email,
        message,
    };
    db.collection("Quries").insertOne(data, (error, docs) => {
        if (error) {
            throw error;
        }
        res.send(
            'Sent successsfully<br/><a href="Register.html " > Retutn LoginPage </a>'
        );
    });
});
app.post("/contactUs", (req, res) => {
    let fisrtName = req.body.firstName;
    let LastName = req.body.lasttName;
    let email = req.body.EmailID;
    let message = req.body.message;

    const data = {
        fisrtName,
        LastName,
        email,
        message,
    };
    db.collection("Contactus").insertOne(data, (error, docs) => {
        if (error) {
            throw error;
        }
        res.send(
            'Sent successsfully<br/><a href="base.html " > Retutn LoginPage </a>'
        );
    });
});