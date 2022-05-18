import React from 'react'
import { connect } from 'react-redux'
import { decrease } from '../redux/componentOne/componentOneActions'

function ComponentOne(props){
  return (
      
    <div>
        componentOne
        <h1>Counts: {props.count}</h1>
        <button onClick={props.decrease}>Decrease</button>
    </div>

  )
}

const mapStateToProps = state =>{
  return{
    count: state.first.count
  }
}

const mapDispatchToProps = dispatch => {
  return{
    decrease : ()=> dispatch(decrease())
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(ComponentOne )