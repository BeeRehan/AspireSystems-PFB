import {React,useContext,useState} from 'react'
import {inputs,selectDoctor,selectVaccinated,selectGender} from './config.js'
import Input from '../../components/atoms/Input/Input.jsx'
import SelectInput from '../../components/atoms/Input/SelectInput'
import Buton from '../../components/atoms/Button/Button.jsx'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'
import { ProfileContext } from '../../index'

export default function CreationForm() {
const profileData = useContext(ProfileContext);
const [state, setState] = useState({
    "Name":profileData.name,
    "Age":profileData.age,
    "Date":"",
    "Time":"",
    "Reason":"",
    "Gender":profileData.gender,
    "File":""
});

let temp;
const handler = (e)=>{
    setState(prevstate=>{
        return{
            ...prevstate,
            [e.target.name]:e.target.value}});
};

function submit(e){
    e.preventDefault()
    console.log(state);
}
    return (
        <>
            <form className="form" onSubmit={submit}>
                <h1>Apply Here</h1>
                {
                    inputs.map((input,ind)=>{
                        const label = input.label;
                        // console.log(stat)
                        if(input.predfined){
                           temp = <Input key={input.label} label={input.label} type={input.type} value={state[label]} onChange={(e)=>handler(e)}  placeholder={input.placeholder} disabled={"disabled"}/>
                        }
                        else{
                            temp = <Input key={input.label} label={input.label} type={input.type} onChange={(e)=>handler(e)}  placeholder={input.placeholder}/>
                        }
                        return(
                           temp 
                        );
                    })
                }
                <SelectInput label="Doctor" onChange={(e)=>handler(e)} option={selectDoctor}/>
                <SelectInput label="Vaccinated" onChange={(e)=>handler(e)} option={selectVaccinated}/>
                <SelectInput label="Gender" onChange={(e)=>handler(e)} option={selectGender} value={state.Gender}/>
                <Wrapper><Buton type="submit" variant="primary" name="Login"/></Wrapper>
            </form>  
        </>
    )
}
