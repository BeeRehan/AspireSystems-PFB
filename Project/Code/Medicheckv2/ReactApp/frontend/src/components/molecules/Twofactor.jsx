import {React,useState} from 'react'
import Cookies from 'universal-cookie'
import jwt from 'jwt-decode';
import {Button, Container} from 'react-bootstrap'
import Input from '../../components/atoms/Input/Input.jsx'
import Buton from '../../components/atoms/Button/Button.jsx'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'
import {useNavigate} from "react-router-dom";

const cookies = new Cookies()
export default function Twofactor() {
    const data = jwt(cookies.get('jwt').jwt)
    const [status, setStatus] = useState()
    const [tfatoken, setTfatoken] = useState({});
    const navigate = useNavigate();
    
    function handle(e){
        setTfatoken(prevstate=>{
            return{
                ...prevstate,
                [e.target.name]:e.target.value}});
    }
// api/verify
    async function submit(e){
        e.preventDefault();
        console.log("ttt:",tfatoken)
        const res = await fetch('http://127.0.0.1:8000/users/api/verify',{
            method:'POST',
            headers:{
                'Content-Type':"application/json",
                "Authorization":cookies.get('jwt')['jwt']
            },
            body: JSON.stringify({
                tfatoken,
                data
            })
        });
        setStatus(await res.json())

        if(status){
            navigate(`/${data.group}`);
        }
        
    }

    return (
        <Container>
            <h1>Welcome to 2 step verifivation</h1>
            <div className="form" >
            <Input label={"Secret Key"} type={'text'} value={data.SecretKey} disabled={"disabled"}/>
            </div>
            <form className="form" onSubmit={submit}>
                <Input label={"OTP"} type={'number'} name={'otp'} placeholder={"OTP"} onChange={(e)=>handle(e)}/>
                <Wrapper><Buton type="submit"  variant="primary" name="Submit"/></Wrapper>
            </form>
        </Container>
    )   
}
