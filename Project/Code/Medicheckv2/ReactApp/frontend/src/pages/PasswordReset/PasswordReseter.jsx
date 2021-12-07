import React from 'react'
import {Container} from 'react-bootstrap'
import Input from '../../components/atoms/Input/Input.jsx'
import {inputs} from "./config.js"
import Buton from '../../components/atoms/Button/Button.jsx'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'

export default function PasswordReseter() {
    return (
        <>
            <Container>
            <h1>Password Page!!!</h1>
            <form className="form" onSubmit={submit}>
                <h1>Login</h1>
                {
                    inputs.map((input,ind)=>{
                        return(
                            <Input key={input.label} label={input.label} type={input.type} onChange={(e)=>handcler(e)}  placeholder={input.placeholder}/>
                        );
                    })
                }
                <Wrapper><Buton type="submit" variant="primary" name="Login"/></Wrapper>
            </form>
            </Container>
        </>
    )
}
