import React,{useState,useEffect} from 'react'
import { Container,Table } from 'react-bootstrap'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'
import {useNavigate} from 'react-router-dom'
import { Button } from 'react-bootstrap';
import Cookies from 'universal-cookie'

const cookies = new Cookies();

export default function Checklist() {
    const [list,setList] = useState([{}]);
    const navigate = useNavigate()

    function fetchUserDetails(){
        fetch(`http://127.0.0.1:8000/checkup/api/create_checklist`,{
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
            setList(data)
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
            <h1>Welcome to Check List Page</h1>
            <Container>
            <TableWrapper color="whitesmoke">
                <Table striped bordered hover>
                    <thead>
                    <tr>
                        <th>Appoinment ID</th>
                        <th>Date</th>
                        <th>User Details</th>
                        <th>Check List</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        list.map((listItem)=>{
                            return(
                                <tr key={listItem.id}>
                                    <td>{listItem.id}</td>
                                    <td>{listItem.date}</td>
                                    <td><Button onClick={()=>
                                    {
                                        navigate(`/doctors/checklist/userdetails/${listItem.user}/${listItem.id}`)
                                    }   
                                    }>UserDetails</Button></td>
                                    <td><Button onClick={()=>
                                    {
                                        navigate(`/doctors/checklist/prescription/${listItem.id}`)
                                    }}>Click Here</Button></td>
                                                    </tr>
                                                );
                                            })
                    }
                    </tbody>
                </Table>
            </TableWrapper>
            {/* Need Home Button Here */}
            </Container>
        </div>
    )
}
