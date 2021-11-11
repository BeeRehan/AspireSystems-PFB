const prom = new Promise((resolve,reject)=>{
    if(true){
        resolve("Resolved");
    }
    else{
        reject("Rejected")
    }
})

prom.then((message)=>{
    console.log(message);
},(message)=>{
    console.log(message);
}).catch(()=>{
    console.log("catch");
})


async function testPromise(){
    const res = await prom
    console.log(`await ${res}`)
}
testPromise()