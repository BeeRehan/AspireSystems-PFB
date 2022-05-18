import React from 'react'
import * as S from './subnavbar.styles'


export default function SubNav() {
  return (
    <>
        <S.secondNav>
            <S.secondNavItem>
                <a href="#fn">
                    Break Fast
                </a>
            </S.secondNavItem>
            <S.secondNavItem>
                <a href="#an">
                    Launch
                </a>
            </S.secondNavItem>
            <S.secondNavItem>
                <a href="#din">
                    Dinner
                </a>
            </S.secondNavItem>
        </S.secondNav>
    </>
  )
}
