import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from './pages/Home/Home';
import Login from './pages/Login/Login.jsx';
import Patient from './pages/Patient/Patient.jsx';
import CreationForm from './pages/Patient/CreationForm';
import Checklist from "./pages/Doctor/Checklist"
import UserDetails from "./pages/Doctor/UserDetails"
import CheckupDetails from "./pages/Doctor/CheckupDetails"
import PreviousCheckup from "./pages/Doctor/PreviousCheckup"
import Doctor from './pages/Doctor/Doctor'
import Admin from './pages/Admin/Admin'
import Myprofile from './pages/Myprofile/Myprofile';
import Logout from './pages/Logout/Logout';
import Unauthorized from './components/universe/Unauthorized.jsx'
import {React, createContext,useState,useEffect,StrictMode} from 'react';
import ReactDOM from 'react-dom';
import reportWebVitals from './reportWebVitals';
import  {BrowserRouter as Router,Routes,Route} from "react-router-dom";
import Cookies from 'universal-cookie';


const cookies = new Cookies();


export const ProfileContext = createContext()
export default function Index() {
  const jwt = cookies.get('jwt')
  const [profileData,setProfileData] = useState({});
  
  useEffect(() => {
    if(jwt){
      fetch("http://127.0.0.1:8000/users/api/api_get_user_profile?Authorization",{
        headers:{
          "Authorization":cookies.get('jwt')['jwt']
      }
      }).then((res)=>{
          if(res.ok){
              return res.json()
          }
          throw res
      }).then((data)=>{
          console.log("Hello",data)
          setProfileData(data)
      }).catch(err=>{
          console.log(err);
  })
  }
  else{
    console.log("JWT Unavailable");
  }
},[]);

// debugger
  return (
    <div>
      <ProfileContext.Provider value={profileData}>
      <Router>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route exact path="/login" element={<Login/>}/>
          {jwt&&(
            <>
              <Route index path="/patients" element={<Patient/>}/>       
              <Route path="/patients/creation" element={<CreationForm/>}/>   
              <Route path="/doctors" element={<Doctor/>}>
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
      </ProfileContext.Provider>
    </div>
  )
}

ReactDOM.render(
  <StrictMode>
    <Index/>
  </StrictMode>,
  document.getElementById('root')
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
