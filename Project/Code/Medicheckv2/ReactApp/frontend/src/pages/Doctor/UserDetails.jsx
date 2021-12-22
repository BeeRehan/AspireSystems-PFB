import React,{useState,useEffect} from 'react'
import { Button, Container,Table } from 'react-bootstrap'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'
import Cookies from 'universal-cookie'
import {useNavigate, useParams, Link} from 'react-router-dom';
import Buton from "../../components/atoms/Button/Button"

const cookies = new Cookies();
export default function UserDetails() {
    const [state,setState] = useState([]);
    const navigate = useNavigate()
    const {pid,aid}  = useParams()

    function fetchUserDetails(){
        fetch(`http://127.0.0.1:8000/appointment/api/get_details/${pid}/${aid}`,{
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

    useEffect(()=>{
        console.log("Useed")
        fetchUserDetails();
    },[]);
 
    return (
        <div>
            <h1>Here is the User Details!!!</h1>
            <Container>
            <TableWrapper color="whitesmoke">
                <Table striped bordered hover>
                    <thead>
                    <tr>
                        <th>Name</th>
                        <th>Date</th>
                        <th>Gender</th>
                        <th>Reason</th>
                        <th>Vaccinated</th>
                        <th>Report</th>
                    </tr>
                    </thead>
                    <tbody>
                        {
                            <tr>
                                <td>{state.name}</td>
                                <td>{state.date}</td>
                                <td>{state.gender}</td>
                                <td>{state.reason}</td>
                                <td>{state.vaccinated}</td>
                                <td><a href={state.report} download>Download</a></td>
                            </tr>
                        }
                    </tbody>
                </Table>
            </TableWrapper>
            
            <Link className='btn' to={`/doctors/checklist/userdetails/previousdetails/${pid}`}><Button>Check Previous checkups</Button></Link>
            
            </Container>
        </div>
    )
}
