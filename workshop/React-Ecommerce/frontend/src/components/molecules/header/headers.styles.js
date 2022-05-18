import { Navbar } from "react-bootstrap";
import styled from 'styled-components'

export const HeaderNav = styled(Navbar)`
    position: relative;
    width: 100%;
    height: 50px;
    background-color:${(props)=>props.bgcolor||'black'}
`;

export const NavItem = styled.div`
    position:absolute;
    right: 0;
    a{
        background-color  : #e6e6e6
        ; 
        text-decoration : None;
        padding : 15px;
    }
    a:hover{
        background-color  : #00f;
        color : #fff
    }
`;