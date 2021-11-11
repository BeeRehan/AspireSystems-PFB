import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import App from './pages/App.js' 
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Renderr from './pages/Lifiting'

function Toroute(){
  return(
    <Router>
      <div>
        <Link to='/'>Home</Link>
      </div>
      <div>
        <Link to='/app'>List</Link>
      </div>
      <div>
        <Link to='/lift'>Lifting</Link>
      </div>
      <hr/>
      <Routes>
        <Route path="/" element={<Tolist/>}/>
        <Route path="/app" element={<App/>}/>
        <Route path="/lift" element={<Renderr/>}/>

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
