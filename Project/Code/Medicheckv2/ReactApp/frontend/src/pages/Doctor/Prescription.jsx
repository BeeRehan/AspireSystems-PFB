import React,{useState} from 'react'
import {Inputs} from "./config.js"
import Buton from '../../components/atoms/Button/Button.jsx'
import Input from '../../components/atoms/Input/Input.jsx'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'
import { useParams,useNavigate } from 'react-router-dom'
import Cookies from 'universal-cookie'

const cookies = new Cookies()
export default function Prescription() {
    const [details, setDetails] = useState({})
    const { aid } = useParams()
    const navigate = useNavigate()

    const handler = (e)=>{
        setDetails(prevstate=>{
            return{
                ...prevstate,
                [e.target.name]:e.target.value}})
    };
    
    function submit(e){
        e.preventDefault()
        console.log("Details:",details)
        fetch(`http://127.0.0.1:8000/checkup/api/post_checklist/${aid}`,{
        method:"POST",
        headers : {
            'Content-Type':"application/json",
            "Authorization":cookies.get('jwt')['jwt'],
        },
        body  : JSON.stringify(details),
        })
        .then(res=>{
            if(res.ok){
                return res.json()
            }
            throw res
        })
        .then(data=>{
            console.log(data);
            navigate('/doctors')
        })
        .catch(er=>{
            console.log("Error:",er)
        })
    
    }    
    
    return (
        <div>
            <form className="form" onSubmit={submit}>
                <h1>Checkip Details</h1>
                {
                    Inputs.map((input,ind)=>{
                        return(
                            <Input key={input.label} label={input.label} type={input.type} onChange={(e)=>handler(e)}  placeholder={input.placeholder}/>
                        );
                    })
                }
                <Wrapper><Buton variant="primary" type="submit" name="Submit"/></Wrapper>
            </form>
        </div>
    )
}
