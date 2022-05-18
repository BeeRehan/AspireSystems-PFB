import React, { Component } from 'react'
import HOC from './HOC' 
class Buttom extends Component {
    constructor(props) {
      super(props)
    }
  render() {
    return (
      <div>Buttom
          Count:{this.props.count}
          <button onClick={this.props.method}>Click</button>
      </div>

    )
  }
}

export default HOC(Buttom)