import styled from 'styled-components'
import { Form } from 'react-bootstrap'

export const formControl = styled(Form.Control)`
    width : 20rem;
    margin : auto;
`

export const formLabel = styled(Form.Label)`
    width : 100px;
    margin-left: 40px;
    margin-top: 40px;
`;

export const formError = styled.span`
    color : #f00;
`;

