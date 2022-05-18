import React, { Component } from 'react'
import {products} from "./constant"
import {useParams} from 'react-router-dom'

export default function ItemDetails() {
  const {name} = useParams();
  let product = {}
  products.forEach((prod,ind)=>{
    if(prod.name===name){
      product = prod
    }
  })
  return (
    <div>itemDetails:{name}
      <h1>Name:{product.name}</h1>
      <h2>Price:{product.price}</h2>
    </div>
  )
}