import React from 'react'
import { Container,Table } from 'react-bootstrap'
import Fetch from './Fetch'
import Navbar from '../../components/universe/Navbar'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'

export default function Doctor() {
    return (
        <div>
            <Navbar  name="Check List" link="/doctors/checklist"/>
            <h1>Welcome Doctor!!!</h1>
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
        </div>
    )
}
