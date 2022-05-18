import styled from 'styled-components'

export const cardWrapper = styled.div`
    position: relative;
    top: 0;
    transition: top ease 0.5s;
    &:hover{
        top: -10px;
    }
`;