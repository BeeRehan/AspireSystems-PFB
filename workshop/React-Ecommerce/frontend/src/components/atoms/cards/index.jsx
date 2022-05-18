import React from 'react'
import { Card,Button, Container, Row,Col } from 'react-bootstrap'
import * as S from './cards.styles'
function CardsList(props) {
  return (
    <S.cardWrapper>
      <Card style={{ width: '15rem', }}>
        <Card.Img variant="top" style={{height:'200px' }} src={props.img} alt="Image not available" />
          <Card.Body>
            <Card.Title>{props.title}</Card.Title>
            <Card.Text>
              Price: {props.price}
            </Card.Text>
            <Card.Text>
            Quantity : {props.quantity}
            </Card.Text>
            <Button variant="primary" onClick={()=>props.addToCart(props)}>Add Cart</Button>
        </Card.Body>
      </Card>
    </S.cardWrapper>
  )
}

export default function Cards({products,addCart}) {
  return (
    <Container>
        <Row id={'fn'}>
          <h1>Break Fast</h1>
          {
            products.filter((product,ind)=>product.category==='fn').map((product,ind)=>{
                return(
                  <Col key={ind}>
                    <CardsList title={product.name} quantity={product.quantity} img={product.image_url} price={product.price} addToCart={addCart}/>
                  </Col>
                )
              })
          }
        </Row>
        <Row id={'an'}>
          <h1>Launch</h1>
          {
            products.filter((product,ind)=>product.category==='an').map((product,ind)=>{
              return(
                <Col key={ind}>
                  <CardsList title={product.name} quantity={product.quantity} img={product.image_url} price={product.price} addToCart={addCart}/>
                </Col>
              )
            })
          }
        </Row>
        <Row id={'din'}>
        <h1>Dinner</h1>
          {
            products.filter((product,ind)=>product.category==='din').map((product,ind)=>{
              return(
                <Col key={ind}>
                  <CardsList title={product.name} quantity={product.quantity} img={product.image_url} price={product.price} addToCart={addCart}/>
                </Col>
              )
            })
          }
        </Row>
    </Container>
  )
}





