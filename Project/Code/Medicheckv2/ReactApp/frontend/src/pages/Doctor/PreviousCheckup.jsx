import React from 'react'
import { Container,Table } from 'react-bootstrap'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'

export default function PreviousCheckup() {
    return (
        <div>
            <h1>Previous Checkups!!!</h1>
            <Container>
            <TableWrapper color="whitesmoke">
                <Table striped bordered hover>
                    <thead>
                    <tr>
                        <th>S. NO</th>
                        <th>Appoinment ID</th>
                    </tr>
                    </thead>
                    <tbody>
                    {/* <Fetch/> */}
                    </tbody>
                </Table>
            </TableWrapper>
            {/* Need Goback Button Here */}
            </Container>
        </div>
    )
}
