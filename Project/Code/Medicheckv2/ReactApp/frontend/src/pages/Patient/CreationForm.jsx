import React from 'react'
import {inputs,selectDoctor,selectVaccinated} from './config.js'
import Input from '../../components/atoms/Input/Input.jsx'
import SelectInput from '../../components/atoms/Input/SelectInput'
import Buton from '../../components/atoms/Button/Button.jsx'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'

export default function CreationForm() {
const handler = ()=>{
    console.log("Form");
};

    return (
        <>
            <form className="form">
                <h1>Apply Here</h1>
                {
                    inputs.map((input,ind)=>{
                        return(
                            <Input key={input.label} label={input.label} type={input.type} onChange={(e)=>handler(e)}  placeholder={input.placeholder}/>
                        );
                    })
                }
                <SelectInput label="Doctor" option={selectDoctor}/>
                <SelectInput label="Vaccinated" option={selectVaccinated}/>
                <Wrapper><Buton type="submit" variant="primary" name="Login"/></Wrapper>
            </form>  
        </>
    )
}
