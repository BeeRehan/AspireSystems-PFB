import React from 'react'
import { Card,Col,Placeholder, Row } from 'react-bootstrap'
export default function SkeletonLoder() {
    let arr = [1,2,3,4,5,6,7,8,9];
  return (
    <Row>
        {
            arr.map((num,ind)=>{
                return(
                <Col xs={4} key={ind}>
                    <Card style={{ width: '18rem' }}>
                        <Card.Img variant="top" />
                        <Card.Body>
                        <Placeholder as={Card.Title} animation="glow">
                            <Placeholder xs={6} />
                        </Placeholder>
                        <Placeholder as={Card.Text} animation="glow">
                            <Placeholder xs={7} /> <Placeholder xs={4} /> <Placeholder xs={4} />{' '}
                            <Placeholder xs={6} /> <Placeholder xs={8} />
                        </Placeholder>
                        <Placeholder.Button variant="primary" xs={6} />
                        </Card.Body>
                    </Card>
                </Col>
                )
            })
        }
    </Row>
  )
}
