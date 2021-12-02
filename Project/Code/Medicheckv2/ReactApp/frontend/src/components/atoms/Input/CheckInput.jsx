import React from 'react'
import { Form,FloatingLabel } from 'react-bootstrap';


export default function CheckInput(props) {
    return (
        <div>
            <Form.Label style={{float:"left",marginBottom:"15px"}}  htmlFor={props.label}>{props.label}</Form.Label>
            <br/>
            <Form.Check
            type={props.type}
            name={props.bvalue}
            label={props.bvalue}
            id={props.label}
            value={props.value}
        />
        </div>
    )
}
