import React, { Component } from 'react'

export default function HOC(OriginalComponent) {
  return class NewComponent extends Component{
      constructor(props) {
        super(props)
      
        this.state = {
           count:0
        }
      }
      incrementCount(){
          this.setState({
            count:this.state.count+1
          },()=>{console.log("Updated!")})
      }
      render(){
          return(
              <>
              <h1>Base Component</h1>
              <OriginalComponent count={this.state.count} method={()=>this.incrementCount()}/>
              </>
          )
      }
  }
}
