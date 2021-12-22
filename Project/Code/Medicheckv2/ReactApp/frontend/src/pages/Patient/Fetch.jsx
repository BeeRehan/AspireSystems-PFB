import React,{useState,useEffect,useContext} from 'react'
import Cookies from 'universal-cookie';
import {Link} from 'react-router-dom'
import { Button } from 'react-bootstrap';

export default function Fetch() {
    const [state,setState] = useState([]);
    const cookies = new Cookies();
  
    useEffect(()=>{
        fetch("http://127.0.0.1:8000/appointment/api/patientt",{
            headers:{
                "Authorization":cookies.get('jwt')['jwt']
            }
        }).then((res)=>{
            if(res.ok){
                return res.json()
            }
            throw res
        }).then((data)=>{
            // console.log("Hello",data)
            setState(data)
        }).catch(err=>{
            console.log(err);
        })
        
    },[]);
    
    return (
            state.map((ste)=>
              <tr key={ste.id}>
                <td>{ste.id}</td>
                <td>{ste.doctor}</td>
                <td>{ste.date}</td>
                <td>{ste.reason}</td>
                <td>{ste.status}</td>
                <td><Link to={`/doctors/checklist/userdetails/checkupupdetails/${ste.id}`}><Button>Click Here</Button></Link></td>
              </tr> )
        );
}
