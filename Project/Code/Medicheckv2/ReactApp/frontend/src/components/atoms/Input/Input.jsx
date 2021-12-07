import React from 'react'
import { Form,FloatingLabel } from 'react-bootstrap';

export default function Input(props) {
    return (
        <div>
            <FloatingLabel controlId={props.label} className="mb-2" label={props.label}>
                <Form.Control type={props.type} name={props.label} value={props.value} placeholder={props.placeholder} onChange={props.onChange} value={props.value} disabled={props.disabled} required/>
            </FloatingLabel>
        </div>
    )
}
