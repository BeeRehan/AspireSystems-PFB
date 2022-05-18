import styled from 'styled-components'

export const secondNav = styled.ul`
    display : flex;
    justify-content : space-evenly;
    border : 1px solid #e6e6e6;
`;

export const secondNavItem = styled.li`
    list-style : none;
    a{
        text-decoration : none;
        text-align : center;
        &:hover{
            background-color : #000;
            color : #fff;
        }
    }
`;