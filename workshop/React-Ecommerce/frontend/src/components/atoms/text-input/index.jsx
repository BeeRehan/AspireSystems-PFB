import React from 'react'
import * as S from './text.styles'

export default function TextInput(props) {
  return (
      <>
        <S.formLabel>{props.label}</S.formLabel>
        <S.formControl
        error={props.error}
          {...props.register(props.name, {...props.validation})}
        />
      </>
  )
}
