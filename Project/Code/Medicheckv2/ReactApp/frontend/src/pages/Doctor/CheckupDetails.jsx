import React from 'react'
import { Container,Table } from 'react-bootstrap'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'

export default function CheckupDetails() {
    return (
        <div>
            <h1>Checkup Details!!!</h1>
            <Container>
            <TableWrapper color="whitesmoke">
                <Table striped bordered hover>
                    <thead>
                    <tr>
                        <th>S. NO</th>
                        <th>Name</th>
                        <th>Date</th>
                        <th>Gender</th>
                        <th>Reason</th>
                        <th>Vaccinated</th>
                        <th>Report</th>
                    </tr>
                    </thead>
                    <tbody>
                    {/* <Fetch/> */}
                    </tbody>
                </Table>
            </TableWrapper>
            {/* Need Go back and Check Previous Checkup Buttons Here */}
            </Container>
        </div>
    )
}
