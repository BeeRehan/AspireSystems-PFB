function goback(){
    window.history.back()
}

function visibility(id){
    console.log(id);
    span = document.getElementById(id);
    span.style.display = "block";
}

function warn(){
    console.log('warn');
    var alert = document.getElementById('alertid');
    alert.style.display = 'block';
}
