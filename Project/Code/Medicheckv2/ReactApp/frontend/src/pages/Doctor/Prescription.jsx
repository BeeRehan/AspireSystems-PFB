import React from 'react'
import {inputs} from "./config.js"
import Buton from '../../components/atoms/Button/Button.jsx'
import Input from '../../components/atoms/Input/Input.jsx'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'

export default function Prescription() {
    return (
        <div>
            <form className="form" onSubmit={submit}>
                <h1>Checkip Details</h1>
                {
                    inputs.map((input,ind)=>{
                        return(
                            <Input key={input.label} label={input.label} type={input.type} onChange={(e)=>handcler(e)}  placeholder={input.placeholder}/>
                        );
                    })
                }
                <Wrapper><Buton type="submit" variant="primary" name="Login"/><Buton variant="primary" name="Go Back"/></Wrapper>
            </form>
        </div>
    )
}
