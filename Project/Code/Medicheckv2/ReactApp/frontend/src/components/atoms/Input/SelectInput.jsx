import React from 'react'
import { Form,FloatingLabel } from 'react-bootstrap';


export default function SelectInput(props) {
    let temp;
    if(props.value){
    return(
        <>   
        <FloatingLabel  className="mb-2" controlId={props.label} label={props.label}> 
        <Form.Select value={props.value} disabled>
            {
                props.option.map((opt)=>{
                    return(
                        <option value={opt.value}>{opt.label}</option>
                    )
                })
            }
        </Form.Select>
        </FloatingLabel>
        </>
    );
    }
    else{
        return(
            <>   
            <FloatingLabel  className="mb-2" controlId={props.label} label={props.label}> 
            <Form.Select onChange={props.onChange}>
                {
                    props.option.map((opt)=>{
                        return(
                            <option value={opt.value}>{opt.label}</option>
                        )
                    })
                }
            </Form.Select>
            </FloatingLabel>
            </>
        );
    }   
}
