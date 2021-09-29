const top1 = document.querySelector("#container1");
//console.log(top1);

const middle = top1.children[0];
//console.log(middle);

const bottom = middle.children[0];

//console.log(middle.firstElementChild.textContent);
//console.log(bottom.textContent);
bottom.textContent = "";

/*---------------------------------------------------------------------------------------------------------*/

const top2 = document.querySelector("#container2");

const middle2 = top2.children[0];

const bottom2 = middle2.children[0];
bottom2.textContent = "Yasin";

/*------------------------------------------------------------------------------------------------------------*/
let studentMark = [{
        name: "rakesh",
        age: "12",
        academics: {
            sslc: "40",
            hsc: "70",
        },
    },
    {
        name: "rakesh",
        age: "12",
        academics: {
            sslc: "60",
            hsc: "70",
        },
    },
    {
        name: "rakesh",
        age: "12",
        academics: {
            sslc: "40",
            hsc: "90",
        },
    },
    {
        name: "rakesh",
        age: "12",
        academics: {
            sslc: "80",
            hsc: "70",
        },
    },
    {
        name: "rakesh",
        age: "12",
        academics: {
            sslc: "59",
            hsc: "20",
        },
    },
    {
        name: "rakesh",
        age: "12",
        academics: {
            sslc: "100",
            hsc: "70",
        },
    },
];

//console.log(studentMark);

//1. List the object which has both mark should be more than 60 average should be 60 //

console.log(
    "1. ",
    studentMark.filter((val, ind, arr) => {
        let hsc = val.academics.hsc;
        let sslc = val.academics.sslc;
        let avg = (Number(hsc) + +sslc) / 2;

        // console.log(avg);
        return hsc > 60 && sslc > 60 && avg == 60; //There is no object equal to 60
    })
);

//2. Should double and display age who got more than 60 as average//
console.log(
    "2. ",
    studentMark.map(function(val, ind, arr) {
        const parent = val.academics;

        let hsc = parent.hsc;
        let sslc = parent.sslc;
        let avg = (Number(hsc) + +sslc) / 2;

        //console.log(avg);
        if (avg > 60) {
            return String(val.age * 2);
        } else {
            return String(val.age);
        }
    })
);

//3. Total the sslc mark and display who got more than 60 as average//

let indi = 0;

let max = +studentMark[0].academics.hsc + +studentMark[0].academics.hsc;

studentMark.forEach((val, ind, arr) => {
    const parent = val.academics;

    let hsc = parent.hsc;
    let sslc = parent.sslc;
    let total = +hsc + +sslc;

    if (max <= total) {
        max = total;
        indi = ind;
    }
});

console.log("3.", "Avg: ", max / 2, "-->", studentMark[indi]);
