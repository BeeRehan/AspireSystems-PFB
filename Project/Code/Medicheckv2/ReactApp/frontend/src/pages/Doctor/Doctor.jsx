import React from 'react'
import { Container,Table } from 'react-bootstrap'
import Fetch from './Fetch'
import Navbar from '../../components/universe/Navbar'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'
import Cookies from 'universal-cookie'


const cookies = new Cookies()
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
                        <th>Date</th>
                        <th>Patient Name</th>
                        <th>Status</th>
                        <th>To Aprove</th>
                        <th>To Reject</th>

                    </tr>
                    </thead>
                    <tbody>
                    <Fetch name={"DocHome"}/>
                    </tbody>
                </Table>
            </TableWrapper>
            </Container>
        </div>
    )
}
