formNode = document.createElement("form");

function addInput(nme, id, clas, type, ph) {
    inputNode = document.createElement("input");
    inputNode.setAttribute("type", type);
    inputNode.setAttribute("name", nme);
    inputNode.setAttribute("id", id);
    inputNode.setAttribute("class", clas);
    inputNode.setAttribute("placeholder", ph);

    return inputNode;
}

function insertSubmit() {
    sdiv = document.createElement("div");
    sButton = document.createElement("button");
    sButton.setAttribute("type", "submit");
    sButton.setAttribute("onsubmit", "validate()");
    sButton.textContent = "Submit";

    sdiv.appendChild(sButton);
    formNode.appendChild(sdiv);
}

function changeBackColor() {
    container.style.backgroundColor = prompt("Enter background color");
}

let container = document.getElementById("formContainer");
// console.log(body);
let ch = Number(prompt("How many Input field you want???"));
let nme, id, type, clas, ph, inputNode;
let div, label, sdiv;

while (ch) {
    div = document.createElement("div");
    label = document.createElement("label");

    nme = prompt("Enter the name of the input tag!!!");
    id = prompt("Enter the id of the input tag!!!");
    type = prompt("Enter the type of the input tag!!!");
    clas = prompt("Enter the class name of the input tag!!!");
    ph = prompt("Enter the place holder name of the input tag!!!");

    inputNode = addInput(nme, id, clas, type, ph);
    label.setAttribute("for", id);
    label.textContent = prompt("Enter the Lable name");

    div.appendChild(label);
    div.appendChild(inputNode);

    formNode.appendChild(div);
    ch -= 1;
}

if (ch == 0) {
    insertSubmit();
}
container.appendChild(formNode);

if (prompt("If you want to change the backgroud??").toLowerCase() == "yes") {
    changeBackColor();
}
