import React from 'react'
import { Form,FloatingLabel } from 'react-bootstrap';


export default function SelectInput(props) {
    return (
        <div>
        <FloatingLabel  className="mb-2" controlId={props.label} label={props.label}> 
        <Form.Select>
            {
                props.option.map((opt)=>{
                    return(
                        <option value={opt.value}>{opt.label}</option>
                    )
                })
            }
        </Form.Select>
        </FloatingLabel>
        </div>
    )
}
