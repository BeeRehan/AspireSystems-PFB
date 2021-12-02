import React,{useState} from 'react'
import "../App.css"
import { useNavigate } from  "react-router-dom";
import Cookies from 'universal-cookie';

export default function Login() {
    const [username,setUsername] = useState("");
    const [password,setPassword] = useState("");
    const[redirect,setRedirect] = useState(false);
    const navigate = useNavigate();
    function submit(e){
        e.preventDefault();
        // try{
        fetch('http://127.0.0.1:8000/users/api/api_login',{
            method : "POST",
            headers : {'Content-Type':"application/json"},
            credentials:"include",
            body  : JSON.stringify({
                username,
                password
            })
        // });
        // console.log(res)
        
        // // setRedirect(true);
        // }
        // catch(err){
        //     console.log(err);
        // }
        }).then(res=>{
            if(res.ok){
                return res.json()
            }
            throw res
        }).then(res=>{
            // console.log(res);
            const cookies = new Cookies();
            cookies.set('jwt', res, { path: '/' });
            console.log(cookies.get('jwt'));
            setRedirect(true);
        }).catch(er=>{
            console.log(er)});
        
    }
    if(redirect){
        navigate("/app");
    }

    return (
        <div>
            <h1>Login</h1>
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
