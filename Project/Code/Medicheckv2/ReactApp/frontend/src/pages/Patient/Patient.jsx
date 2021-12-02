import React from 'react'
import { Container,Table } from 'react-bootstrap'
import Patientnavbar from '../../components/universe/patientNavbar'
import Fetch from './Fetch'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'

export default function Patient() {
    return (
        <>
            <Patientnavbar/>
            <h1>Welcome to Patient Page</h1>
            <Container>
            <TableWrapper color="whitesmoke">
                <Table striped bordered hover>
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Doctor</th>
                        <th>Date</th>
                        <th>Reason</th>
                        <th>Status</th>
                    </tr>
                    </thead>
                    <tbody>
                    <Fetch/>
                    </tbody>
                </Table>
            </TableWrapper>
            </Container>
        </>
    )
}
