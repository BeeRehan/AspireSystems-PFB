import React from 'react'
import {Carousel} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import slide1 from "../../static/images/slide1.jpg"
import slide2 from "../../static/images/slide2.jpg"
import slide3 from "../../static/images/slide3.jpg"

export default function Carousell() {
    return (
            <Carousel fade>
            <Carousel.Item interval={1000}>
                <img
                className="d-block w-100"
                src={slide1}
                alt="First slide"
                />
                <Carousel.Caption>
                <h3>24/7 Service</h3>
                <p>We Provide 24/7 service for the client!!!</p>
                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item interval={500}>
                <img
                className="d-block w-100"
                src={slide2}
                alt="Second slide"
                />
                <Carousel.Caption>
                <h3>Quality Doctors</h3>
                <p>We have the world quality doctors!!!</p>
                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item interval={500}>
                <img
                className="d-block w-100"
                src={slide3}
                alt="Second slide"
                />
                <Carousel.Caption>
                <h3>Quality Eqiupments</h3>
                <p>We have the world quality equipments!!!</p>
                </Carousel.Caption>
            </Carousel.Item>
            </Carousel>
    )
}
