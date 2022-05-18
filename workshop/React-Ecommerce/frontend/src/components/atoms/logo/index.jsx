import logo from 'assets/y-logo.png'
import React from 'react'
import * as S from './logo.styles'
export default function Logo(props) {
  return (
    <S.AppLogo
    src={logo}
    alt={"Logo not found"}
    width={props.width}
    />
  )
}
