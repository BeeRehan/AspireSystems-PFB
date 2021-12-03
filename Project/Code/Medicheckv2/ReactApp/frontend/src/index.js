import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from './pages/Home/Home';
import Login from './pages/Login/Login.jsx';
import Patient from './pages/Patient/Patient.jsx';
import CreationForm from './pages/Patient/CreationForm';
import Checklist from "./pages/Doctor/Checklist"
import UserDetails from "./pages/Doctor/UserDetails"
import CheckupDetails from "./pages/Doctor/CheckupDetails"
import Checklist from "./pages/Doctor/Checklist"
import PreviousCheckup from "./pages/Doctor/PreviousCheckup"
import Doctor from './pages/Doctor/Doctor'
import Admin from './pages/Admin/Admin'
import Myprofile from './pages/Myprofile/Myprofile';
import Logout from './pages/Logout/Logout';
import Unauthorized from './components/universe/Unauthorized.jsx'
import React from 'react';
import ReactDOM from 'react-dom';
import reportWebVitals from './reportWebVitals';
import  {BrowserRouter as Router,Routes,Route} from "react-router-dom";
import Cookies from 'universal-cookie';


const cookies = new Cookies();
export default function Index() {
  const jwt = cookies.get('jwt')
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route exact path="/login" element={<Login/>}/>
          {jwt&&(
            <>
              <Route path="/patients">   
                <Route path="/patients" element={<Patient/>}/>
                <Route path="creation" element={<CreationForm/>}/>       
              </Route>
              <Route path="/doctors">
                <Route path="/doctors" element={<Doctor/>}/>          
                <Route path="checklist" element={<Checklist/>}/>
                <Route path="userdetails" element={<UserDetails/>}>
                  <Route path="previousdetails" element={<PreviousCheckup/>}>
                  <Route path="checkupupdetails" element={<CheckupDetails/>}/>
                  </Route>
                </Route> 
              </Route>
              <Route path="/admin" element={<Admin/>}>          
              </Route>
              <Route path="/myprofile" element={<Myprofile/>}/>
            </>
          )
          }
          <Route path="/logout" element={<Logout/>}/>
          <Route path="/:pageName" element={<Unauthorized/>}/>
        </Routes>
      </Router>
    </div>
  )
}


ReactDOM.render(
  <React.StrictMode>
    <Index/>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
