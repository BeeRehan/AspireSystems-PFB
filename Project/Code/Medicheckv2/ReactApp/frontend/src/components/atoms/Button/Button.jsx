import React from 'react'
import { Button } from 'react-bootstrap'

export default function Buton(props) {
    return (
        <div>
            <Button type={props.type} onClick={props.onClick} variant={props.variant}>{props.name}</Button>
        </div>
    )
}
