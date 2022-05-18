import React from 'react'
import { FieldMapper } from './constants'

export default function Field(props) {
      const Compounent = FieldMapper[props.type]
  return (
    <Compounent {...props}/>
  )
}
