import {React,useState} from 'react'
import Input from '../../components/atoms/Input/Input.jsx'
import {inputs} from "./config.js"
import Buton from '../../components/atoms/Button/Button.jsx'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'
import {useNavigate} from "react-router-dom";
import Cookies from 'universal-cookie';
import jwt from 'jwt-decode';

export default function Login() {
    const [state, setState] = useState({
        "Username":"",
        "Password":""
    });

    const [user,setUser] = useState({})
    const[redirect,setRedirect] = useState(false);
    const navigate = useNavigate();

    const handcler = (e)=>{
        setState(prevstate=>{
            return{
                ...prevstate,
                [e.target.name]:e.target.value}});
    };

    function submit(e){
        e.preventDefault();
        const username = state.Username;
        const password = state.Password;
        // console.log("Check",process.env.REACT_APP_API_LOGIN)
        fetch("http://127.0.0.1:8000/users/api/api_login",{
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
            // console.log(res);
            const cookies = new Cookies();
            cookies.set('jwt', res, { path: '/' });
            setUser(jwt(cookies.get('jwt').jwt))
            console.log(cookies.get('jwt'),);
            setRedirect(true);
        }).catch(er=>{
            console.log(er)});    
    }

    if(redirect){
        navigate(`/${user.group}`);
    }

    return (
        <>
            <h1>Welcome to Login Page!!!</h1>
            <form className="form" onSubmit={submit}>
                <h1>Login</h1>
                {
                    inputs.map((input,ind)=>{
                        return(
                            <Input key={input.label} label={input.label} type={input.type} onChange={(e)=>handcler(e)}  placeholder={input.placeholder}/>
                        );
                    })
                }
                <Wrapper><Buton type="submit"  variant="primary" name="Login"/></Wrapper>
            </form>
        </>
    )
}
