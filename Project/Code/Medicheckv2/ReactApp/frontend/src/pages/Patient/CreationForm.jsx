import {React,useContext,useState,useEffect} from 'react'
import {inputs,selectDoctor,selectVaccinated,selectGender} from './config.js'
import Input from '../../components/atoms/Input/Input.jsx'
import SelectInput from '../../components/atoms/Input/SelectInput'
import Buton from '../../components/atoms/Button/Button.jsx'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'
import { ProfileContext } from '../../index'
import Cookies from 'universal-cookie'
import { Navigate, useNavigate } from 'react-router-dom'


const cookies = new Cookies();
export default function CreationForm() {
const profileData = useContext(ProfileContext);
const [state, setState] = useState({});
const navigate = useNavigate();

const  data ={
 "Name" : profileData.name,
 "Age" : profileData.age,
 "Gender" : profileData.gender,
}

let temp;
const handler = (e)=>{
    setState(prevstate=>{
        return{
            ...prevstate,
            [e.target.name]:e.target.value}});
    
    setState(prevstate=>{
        return{
            ...prevstate,
            ...data}});
    
};

function submit(e){
    e.preventDefault()
    console.log("Application Details",state);
    fetch('http://127.0.0.1:8000/appointment/api/apply_appoinment',{
    method:"POST",
    headers : {
        'Content-Type':"application/json",
        "Authorization":cookies.get('jwt')['jwt'],
    },
    body  : JSON.stringify(state),
    })
    .then(res=>{
        if(res.ok){
            return res.json()
        }
        throw res
    })
    .then(data=>{
        console.log(data);
        navigate('/patients')
    })
    .catch(er=>{
        console.log("Error:",er)
    })

}
    return (
        <>
            <form className="form" onSubmit={submit}  enctype="multipart/form-data">
                <h1>Apply Here</h1>
                {
                    inputs.map((input)=>{
                        const label = input.label;
                        // console.log(stat)
                        if(input.predfined){
                           temp = <Input key={input.label} label={input.label} type={input.type} value={data[label]} onChange={(e)=>handler(e)}  placeholder={input.placeholder} disabled={"disabled"}/>
                        }
                        else{
                            temp = <Input key={input.label} label={input.label} type={input.type} onChange={(e)=>handler(e)}  placeholder={input.placeholder}/>
                        }
                        return(
                           temp 
                        );
                    })
                }
                <SelectInput label="Doctor" name="Doctor" onChange={(e)=>handler(e)} option={selectDoctor}/>
                <SelectInput label="Vaccinated" name="Vaccinated" onChange={(e)=>handler(e)} option={selectVaccinated}/>
                <SelectInput label="Gender" onChange={(e)=>handler(e)} option={selectGender} value={data.Gender}/>
                <Wrapper><Buton type="submit" variant="primary" name="Login"/></Wrapper>
            </form>  
        </>
    )
}
