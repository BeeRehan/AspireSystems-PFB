import {React,Component} from "react";

export default class CondionalRendering extends Component{
    constructor(props){
        super(props)
    }
    render(){

        if(this.props.status){
            return (
                <>    
                    <h1 style={{color:"#0f0"}}>Status True</h1>
                </>
            );    
        }
        else{
            return(
                <>
                    <h1 style={{color:"#f00"}}>Status False</h1>
                </>
            );
        }
          
    }
}