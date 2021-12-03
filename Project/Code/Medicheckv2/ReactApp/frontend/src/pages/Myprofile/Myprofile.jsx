import React from 'react'
import {inputs} from "./config.js"
import Input from '../../components/atoms/Input/Input.jsx'
import Buton from '../../components/atoms/Button/Button.jsx'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'

export default function Myprofile() {
    return (
        <div>
            <form className="form">
                <h1>My Profile</h1>
                {
                    inputs.map((input,ind)=>{
                        return(
                            <Input key={input.label} label={input.label} type={input.type}  placeholder={input.placeholder}/>
                        );
                    })
                }
                <Wrapper><Buton type="submit" variant="primary" name="Login"/></Wrapper>
            </form>
        </div>
    )
}
