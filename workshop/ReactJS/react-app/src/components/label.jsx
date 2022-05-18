import React, { Component } from 'react'
import HOC from './HOC'
class Label extends Component {
    constructor(props) {
      super(props)
    }
  render() {
    return (
      <div onMouseOver={this.props.method}>label<br/>
          Count:{this.props.count}
      </div>
    )
  }
}


export default HOC(Label);
