import React, { Component } from 'react'
import {Link,NavLink} from 'react-router-dom';
export default class Nav
 extends Component {
  render() {
    return (
      <div>
        <nav className='nav'>
            <ul>
                <NavLink  style={({ isActive }) => {
              return {
                color: isActive ? "red" : "Green",
              };
            }} to="/"><li>Home</li></NavLink>
                <Link to="shop"><li>Shop</li></Link>
                <Link to="moperators"><li>Mobile Operators</li></Link>
                <Link to="contact"><li>Contact</li></Link>
            </ul> 
        </nav>     
      </div>
    )
  }
}
