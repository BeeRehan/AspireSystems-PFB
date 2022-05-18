import Header from 'components/molecules/header'
import { AuthService } from 'core/auth.service'
import React from 'react'
import { Table,Alert,Button } from 'react-bootstrap'

export default function Cart({items,changeQuantity,removeItem}) {
  const total = items.reduce((sum,item)=>sum+Number(item.price)*Number(item.quantity),0)
  const status = AuthService.getToken() || false;
  return (
    <div>
      <Header/>
      <h1>Cart Items</h1> 
      <Table striped bordered hover>
        <thead>
          <tr>
            <th colSpan={2}>Name</th>
            <th>Quantity</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
      {items.map((item,ind)=>{
        return(
            <tr key={ind}>
              <td>
                <span style={{display:"flex",justifyContent:"space-around"}}>
                <img style={{width:"50px",height:"50px"}} src={item.img} alt="Not found"/>
                </span>
              </td>
              <td>
                <p style={{margin:"10px"}}>{item.title}</p>
              </td>
              <td>
                <Button onClick={() => changeQuantity(item, 1)}>+</Button>
                <Button disabled>{item.quantity}</Button>
                <Button onClick={() => changeQuantity(item, (((item.quantity-1)===0)?0:-1))}>-</Button>
              </td>
              <td>
                <span style={{display:"flex",justifyContent:"space-around"}}>
                  <p style={{margin:"10px"}}>{item.price*item.quantity}</p>
                  <Button onClick={()=>removeItem(item.title)}>Remove</Button>
                </span>
              </td>
            </tr>
          )
        })}
        </tbody>
        </Table>
        <hr />
        <Alert variant="success">
  <Alert.Heading>Bill</Alert.Heading>
  <hr />
  <div style={{display:"flex",justifyContent:"space-evenly"}}>
    <p>Total</p>
    <p>{total}</p>
  </div>
</Alert>
  <div style={{margin:"auto",width: "200px"}}>
    {status&&
      <>
        <Button onClick={alert("Order Placed!!!")}>Buy Now</Button>
      </>
    }
    {!status&&
      <>
        <Button onClick={()=>{window.location.replace('/signin')}}>Login to Buy</Button>x
      </>
    }
  </div>
  </div>
  )
}
