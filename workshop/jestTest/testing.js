import fetch from 'node-fetch';
import axios from 'axios';

async function toHome(){
    const val = await axios.get('https://jsonplaceholder.typicode.com/todos/1')
    console.log(val);
    return val.data;
}

console.log("Hello")
const res = toHome()
console.log(res)
console.log("World")