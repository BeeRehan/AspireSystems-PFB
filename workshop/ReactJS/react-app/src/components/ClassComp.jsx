import {React,Component}  from 'react'

export default class ClassComp extends Component {
    constructor(props){
        super(props)
        this.state = {
            name : ""
        }
        this.handleOnChange = this.handleOnChange.bind(this)
    }
    handleOnChange(e){
        {console.log("val",e.target.value);}
        this.setState({
            name:e.target.value
        })
    } 
  render() {
    return (
      <div>
          Entere the name: <input type={'text'} name={"username"} onChange={this.handleOnChange} value={this.state.name}/>
          <br/>
        Class Component:{this.props.name}-{this.state.name}
        </div>
    )
  }
}
