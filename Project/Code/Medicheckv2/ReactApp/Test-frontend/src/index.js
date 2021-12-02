import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './pages/App';
import Login from './pages/Login.jsx';
import Result from './pages/Result';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter  as Router,Routes,Route,Link} from "react-router-dom";
import Cookies from 'universal-cookie';
import Logout from './pages/Logout';
import Register from './pages/Register';

const cookies = new Cookies();

function Index() {
  let navBar;

  if(cookies.get('jwt')){
    navBar = (    
    <div>
      <ul>
      <li><Link to="/">Home</Link></li>
      <li><Link to="/logout">Logout</Link></li>
    </ul>
    </div>
    )
  }
else{
  navBar=(
  <div>
  <ul>
  <li><Link to="/">Home</Link></li>
  <li><Link to="/register">Register</Link></li>
  <li><Link to="/login">LogIn</Link></li>
</ul>
</div>)
}
  return (
    <>
    {navBar}
    </>
  )
}


ReactDOM.render(
  <React.StrictMode>
  <Router>
    <Index/>
    <Routes>
      <Route path='/' element={<App/>}/>
      <Route path='/login' element={<Login/>}/>
      <Route path='/register' element={<Register/>}/>
      <Route path='/logout' element={<Logout/>}/>
      <Route path='/app' element={<Result/>}/>
    </Routes>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
