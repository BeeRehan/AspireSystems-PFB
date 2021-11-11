import { useState } from "react";

function Renderr(){
    const [state,setState] = useState("HI");
    return(
        <>
            <Type setState={setState}/>
            <Display state={state}/>
        </>
    );
}

function Type({setState}){
    function change(e){
        setState(e.target.value);
    }
    return(
        <>
            <input onChange={change}/>
        </>
    );
}

function Display({state}){
    return(
        <>
            <h1>{state}</h1>
        </>
    );
}

export default Renderr;