function sayHello(a){
    console.log(a) ;
    console.log("Hello");
    a()
}


sayHello(sayWorld)

function sayWorld(){
    console.log("world");
}
