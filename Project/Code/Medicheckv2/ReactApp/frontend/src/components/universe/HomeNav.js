import React from 'react'
import { Container,Navbar,Nav,Offcanvas } from 'react-bootstrap';
import {Link} from "react-router-dom";

export default function HomeNav() {
    return (
        <div>
        <Navbar bg="primary" expand={false}>
            <Container fluid>
            <Navbar.Toggle aria-controls="offcanvasNavbar" />
            <Navbar.Offcanvas
                id="offcanvasNavbar"
                aria-labelledby="offcanvasNavbarLabel"
                placement="end"
            >
                <Offcanvas.Header closeButton>
                <Offcanvas.Title id="offcanvasNavbarLabel">To Access</Offcanvas.Title>
                </Offcanvas.Header>
                <Offcanvas.Body>
                <Nav className="justify-content-end flex-grow-1 pe-3">
                    <Nav.Link as={Link} to="/login">Login</Nav.Link>
                </Nav>
                </Offcanvas.Body>
            </Navbar.Offcanvas>
            </Container>
        </Navbar>
        </div>
    )
}
