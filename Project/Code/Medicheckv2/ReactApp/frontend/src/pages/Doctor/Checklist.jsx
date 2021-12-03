import React from 'react'
import { Container,Table } from 'react-bootstrap'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'

export default function Checklist() {
    return (
        <div>
            <h1>Welcome to Check List Page</h1>
            <Container>
            <TableWrapper color="whitesmoke">
                <Table striped bordered hover>
                    <thead>
                    <tr>
                        <th>S. NO</th>
                        <th>Appoinment ID</th>
                        <th>Date</th>
                        <th>User Details</th>
                        <th>Check List</th>
                    </tr>
                    </thead>
                    <tbody>
                    {/* <Fetch/> */}
                    </tbody>
                </Table>
            </TableWrapper>
            {/* Need Home Button Here */}
            </Container>
        </div>
    )
}
