import './App.css';
import {useEffect, useMemo, useRef, useState,useReducer} from "react";

function UseState(){
  const [state,setState] = useState({name:"Yasin",age:20});

  function change(){
    setState((prevState)=>{
      return{...prevState,name:"md"}
    });
  }
return(
  <>
  <h1>UseState-Hello {state.name} with age {state.age}</h1> 
  <button onClick={change}>To change</button>
  <hr/>
  </>);
}

function UseEffect(){
  const [width,setState] = useState(window.innerWidth)
  function change(){
    setState(window.innerWidth)
  }
  useEffect(
    ()=>{
      window.addEventListener('resize',change)

      return ()=>{
        window.removeEventListener('resize',change)
      };
    },[width]);
  return(
    <>
      <h1>useEffect-The width is: {width}</h1>
      <hr/>
    </>
  );
}

function UseMemo(){
  const [state,setState] = useState(1);
  const number = useMemo(()=>{
    return multiply(state);
  },[state])
  function change (){
    setState((prev)=>{
      return prev+1;
    })
  }
  function multiply(num){
    console.log("No memo");
    return num*2;
  }
return(<>
  <h1>useMemo-{number}</h1>
  <input type="number" value={state} onChange={(e)=>{setState(parseInt(e.target.value))}} min={0} />
  <button onClick={change}>Click</button>
  <hr/>
</>);
}

function UseRef(){
  const [state,setState] = useState("");
  const prevState = useRef("");

  useEffect(()=>{
    prevState.current=state;
  },[state]);

  return(<>
  <input type="text" value={state} onChange={(e)=>setState(e.target.value)}/>
  <h1>UseRef-current State={state} |Previous state-{prevState.current} </h1>
  <hr/>
  </>);
}

const ACTION = {
  INCREAMENT : "Increament",
  DECREAMENT : "decreament",
};

function UseReducer(){
  function reducer(state,action){
    switch(action.type){
      case ACTION.INCREAMENT:
        return state+1; 
      case ACTION.DECREAMENT:
        return state-1;
      default:
        return state;
    }
  }
  const [count,change] = useReducer(reducer,0)
  function inchange(){
    change({type:ACTION.INCREAMENT});
  }
  function dechange(){
    change({type:ACTION.DECREAMENT});
  }
  return(
    <>
    <h1>useReducer- {count}</h1>
    <button onClick={inchange}>Increament</button>
    <button onClick={dechange}>Decreament</button>
    <hr/>
    </>
  );
}

function App() {
  return (
    <div className="App">
      <UseState/>
      <UseEffect/>
      <UseMemo/>
      <UseRef/>
      <UseReducer/>
    </div>
  );
}

export default App;
