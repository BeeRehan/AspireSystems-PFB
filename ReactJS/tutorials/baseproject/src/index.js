import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import App from './App.js' 
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

export default function Toroute(){
  return(
    <Router>
      <div>
        <Link to='/'>Home</Link>
      </div>
      <div>
        <Link to='/list'>List</Link>
      </div>
      <hr/>
      <Routes>
        <Route exact path="/">
          <Tolist/>
        </Route>
        <Route path="/list">
          <App/>
        </Route>
      </Routes>
    </Router>
  );
}
function Home(props){
  return <li>{props.pname}</li>;
}

function Tolist(props){
  const names =["Yasin","MD","Mohamed"]
  return (
  <>
    <ul>
      {names.map((name)=> <Home key={name} pname={name}/>)}
    </ul>
  </>);
}
ReactDOM.render(
  <Toroute />,
  document.getElementById('root')
);

reportWebVitals();
