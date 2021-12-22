import {React,useContext,useState, useEffect} from 'react'
import {inputs} from "./config.js"
import Input from '../../components/atoms/Input/Input.jsx'
import Buton from '../../components/atoms/Button/Button.jsx'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'
import { ProfileContext } from '../../index'
import Cookies from 'universal-cookie'
import { useNavigate } from 'react-router-dom'

const cookies = new Cookies()
export default function Myprofile() {
    const profileData = useContext(ProfileContext);
    const data ={
        "Username":profileData.name,
        "Group":profileData.group,
        "Age":profileData.age,
        "Secret Key":profileData.key
    };
    let temp;
    const navigate = useNavigate();
    const [details, setDetails] = useState({...data});


    const handler = (e)=>{
        setDetails(prevstate=>{
            return{
                ...prevstate,
                [e.target.name]:e.target.value}});
        
        setDetails(prevstate=>{
            return{
                ...prevstate,
            "Username":profileData.name,
            "Group":profileData.group,}});
    };
    
    function submit(e){
        e.preventDefault()
        console.log("Details:",details)
        fetch('http://127.0.0.1:8000/users/api/post_user_profile',{
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
            navigate('/myprofile')
        })
        .catch(er=>{
            console.log("Error:",er)
        })
    
    }    

    return (
        <div>
            <form className="form" onSubmit={submit}>
                <h1>My Profile</h1>
                {
                    inputs.map((input,ind)=>{
                        
                        if(input.predefined){
                            temp = <Input key={input.label} label={input.label} type={input.type} value={data[input.label]} onChange={(e)=>handler(e)} placeholder={input.placeholder} disabled={"disabled"}/>
                        }
                        else{
                           temp = <Input key={input.label} label={input.label} type={input.type} value={details[input.label]} onChange={(e)=>handler(e)} placeholder={input.placeholder}/>
                        }
                        
                        return(
                            temp
                        );
                    })
                }
                <Wrapper><Buton type="submit" variant="primary" name="Submit"/></Wrapper>
            </form>
        </div>
    )
}
