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
        return res.redirect("base.html");
    })
    .listen(3031);

app.post("/registration", (req, res) => {
    let emailId = req.body.emailID;
    let password = req.body.password;
    let repassword = req.body.repassword;
    let district = req.body.password;

    let data = {
        emailId,
        password,
        repassword,
        district,
    };

    db.collection("users").insertOne(data, (err, collection) => {
        if (err) {
            throw err;
        }
        console.log("Record Inserted Successfully");
    });

    return res.redirect("signup_success.html");
});