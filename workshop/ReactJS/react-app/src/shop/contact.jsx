import React, { Component } from 'react'

export default class Contact extends Component {
  constructor(props) {
    super(props)
  
    this.state = {
      field:{},
      error:{}
        
    }
  }
  changeFields(e){
    console.log("Entered",this.state);
    let field = this.state.field;
    field[e.target.name] = e.target.value;
    this.setState(field);
  }
  submitedForm(e){
    e.preventDefault()
    if(this.validateForm()){
      let field={};
      this.setState(field)
      console.log("validated",this.state)
    }
    else{
      console.log("Validated",this.state)
    }
  }
  validateForm(e){
    let field=this.state.field;
    let error = {};
    let isValid = true;
    if(!field["name"]){
      isValid = false;
      error.name = "ENter Name";
    }
    if(!field["feedback"]){
      isValid = false;
      error.feedback = "ENter feedback";
    }
    this.setState({
      error:error
    })
    console.log("Validatesd",this.state)
    return(isValid)
  }
  render() {
    return (
      <div>contact
        <form action="" method='POST' name='contactform' onSubmit={(e)=>this.submitedForm(e)}>
          <label htmlFor="name">Name</label> <br/> {this.state.error.name}<br/>
          <input type="text" id='name' name='name' value={this.state.field.name} onChange={(e)=>this.changeFields(e)}/><br/>
          <label htmlFor="feedback">Feedback</label><br/>{this.state.error.feedback}<br/>
          <input type="text" name='feedback' value={this.state.field.feedback} onChange={(e)=>this.changeFields(e)}/><br/>
          <button type='submit'>Submit</button>

        </form>
      </div>
    )
  }
}
