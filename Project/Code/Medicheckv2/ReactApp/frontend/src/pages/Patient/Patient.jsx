import React from 'react'
import { Container,Table } from 'react-bootstrap'
import Navbar from '../../components/universe/Navbar'
import Fetch from './Fetch'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'

export default function Patient() {
    return (
        <>
            <Navbar  name="Apply New" link="/patients/creation"/>
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
