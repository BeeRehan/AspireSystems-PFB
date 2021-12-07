import React, { useContext } from 'react'
import { Container,Table } from 'react-bootstrap'
import Navbar from '../../components/universe/Navbar'
import Fetch from './Fetch'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'
import { ProfileContext } from '../../index'

export default function Patient() {
    const profileData = useContext(ProfileContext);
    console.log("Profile",profileData);
    return (

        <>
            <Navbar  name="Apply New" link="/patients/creation"/>
            <Container>
            <h1>Welcome to Patient Page</h1>
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
