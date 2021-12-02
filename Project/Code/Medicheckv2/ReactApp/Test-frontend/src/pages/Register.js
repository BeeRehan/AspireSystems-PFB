import React,{useState} from 'react'
import { useNavigate } from  "react-router-dom";

export default function Register() {
    const [username,setUsername] = useState("");
    const [password,setPassword] = useState("");
    const[redirect,setRedirect] = useState(false);
    const navigate = useNavigate();
    function submit(e){
        e.preventDefault();
        fetch('http://127.0.0.1:8000/users/api/api_register',{
            method : "POST",
            headers : {'Content-Type':"application/json"},
            credentials:"include",
            body  : JSON.stringify({
                username,
                password
            })
        }).then(res=>{
            if(res.ok){
                return res.json()
            }
            throw res
        }).then(res=>{
            console.log(res);
            setRedirect(true);
        }).catch(er=>{
            console.log(er)});
        
        }
        if(redirect){
            navigate("/");
        }
    
    return (
        <div>
            <h1>Register</h1>
            <form onSubmit={submit}>
                <pre>
                <label>Username</label>
                <input type="text" onChange={e=>setUsername(e.target.value)} required/>
                <br/>
                <label>Password</label>
                <input type="password" onChange={e =>setPassword(e.target.value)} required/>
                <br/>
                <input type="submit"/>
                </pre>
            </form>
        </div>
    )
}
