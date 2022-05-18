import React, { Component } from 'react'
import {Link, Outlet} from 'react-router-dom'
class Listitems extends Component {
  constructor(props) {
    super(props)
  }
  render() {
    return (
     <ul>
       {this.props.items.map((item,ind)=>{
         return(
          <Link to={item} key={ind}><li>{item}</li></Link>
         )
       })}
     </ul>
    );
  }
}

export default class Items extends Component {
    constructor(props) {
      super(props)
    
      this.state = {
         products : ["product", "product2", "product3", "product4", ]
      }
    }
    
  render() {
    return (
      <div>items
        <Listitems items={this.state.products}/>
        <Outlet/>
      </div>

    )
  }
}
