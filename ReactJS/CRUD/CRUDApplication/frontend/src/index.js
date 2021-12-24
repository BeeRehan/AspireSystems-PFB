import {React,StrictMode} from 'react'
import ReactDOM from 'react-dom';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter as Router, Routes,Route} from 'react-router-dom'

import Home from './pages/Home'
import List from './pages/List'
import Edit from './pages/Edit'

ReactDOM.render(
  <StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/list" element={<List/>} />
        <Route path="/edit/:id" element={<Edit/>} />
      </Routes>
    </Router>
  </StrictMode>,
  document.getElementById('root')
);

reportWebVitals();








