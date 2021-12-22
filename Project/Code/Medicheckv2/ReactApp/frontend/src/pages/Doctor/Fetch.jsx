import React,{useState,useEffect} from 'react'
import { Button } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import Cookies from 'universal-cookie';
import jwt from 'jwt-decode';

export default function Fetch(props) {
    const [state,setState] = useState([]);
    const cookies = new Cookies();
    const navigate = useNavigate()
    const [user,setUser] = useState({})

    useEffect(()=>{
        console.log("Fetching......")
        fetchData() 
        setUser(jwt(cookies.get('jwt').jwt))       
    },[])

    // console.log(user)
    function fetchData(){
        fetch("http://127.0.0.1:8000/appointment/api/doctor",{
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
            setState(data)
        }).catch(err=>{
            console.log(err);
        })
    }
    
    function approve(id){
        fetch(`http://127.0.0.1:8000/appointment/api/approve/${id}`,{
            method:"POST",
            headers:{
                "Authorization":cookies.get('jwt')['jwt']
            }
        })
        .then(res=>{
            if(res.ok){
                return(res.json())
            }
            throw res
        })
        .then(res=>{
            console.log(res)
            fetchData()
        })
        .catch(er=>{
            console.log("Error:",er);
        })
    }

    function reject(id){
        fetch(`http://127.0.0.1:8000/appointment/api/reject/${id}`,{
            method:"POST",
            headers:{
                "Authorization":cookies.get('jwt')['jwt']
            }
        })
        .then(res=>{
            if(res.ok){
                return(res.json())
            }
            throw res
        })
        .then(res=>{
            console.log(res)
            fetchData()
        })
        .catch(er=>{
            console.log("Error:",er);
        })
    }

    console.log("Name:",props.name)
    if(props.name==="DocHome")
        return (
                state.map((ste)=>
                <tr key={ste.id}>
                    <td>{ste.id}</td>
                    <td>{ste.date}</td>
                    <td>{ste.name}</td>
                    <td>{ste.status}</td>
                    <td><Button onClick={(id)=>approve(ste.id)}>Approve</Button></td>
                    <td><Button onClick={(id)=>reject(ste.id)}>Reject</Button></td>
                </tr> )
            );
    
    if(props.name==='checklist'){
        return(
            state.map((ste)=>
                <tr key={ste.id}>
                <td>{ste.id}</td>
                <td>{ste.date}</td>
                <td>{ste.status}</td>
                <td><Button onClick={()=>
                {
                    navigate(`/doctors/checklist/userdetails/${ste.user_id}/${ste.id}`)
                }
                }>UserDetails</Button></td>
                <td><Button onClick={()=>
                {
                    navigate(`/doctors/checklist/prescription/${ste.id}`)
                }}>Click Here</Button></td>
            </tr> ));
    }

    if(props.name==='userprofile'){
        return(
            state.map((ste)=>
                <tr key={ste.id}>
                <td>{ste.id}</td>
                <td>{ste.date}</td>
                <td><Button onClick={()=>
                {
                    navigate('/doctors/checklist/userdetails')
                }
                }>UserDetails</Button></td>
                <td><Button onClick={()=>
                {
                    navigate(`/doctors/checklist/prescription/${ste.id}`)
                }}>Click Here</Button></td>
            </tr> ));
    }
}
