import {React,useState,useEffect} from 'react'
import { Container,Table } from 'react-bootstrap'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'
import {useParams} from 'react-router-dom'
import Cookies from 'universal-cookie'


const cookies = new Cookies()
export default function CheckupDetails() {
    const [prescription, setPrescription] = useState({});
    const {pid} = useParams();

    function fetchPreviousCheckup(){
        fetch(`http://127.0.0.1:8000/checkup/api/get_checklist/${pid}`,{
            headers:{
                "Authorization":cookies.get('jwt')['jwt']
            }
        }).then((res)=>{
            if(res.ok){
                return res.json()
            }
            throw res
        }).then((data)=>{
           console.log("Setting Data")
           setPrescription(data)
        }).catch(err=>{
            console.log(err);
        })
    }

    useEffect(()=>{
        console.log("fetching........")
        fetchPreviousCheckup();
    },[]);
    console.log(prescription)
    return (
        <div>
            <h1>Checkup Details!!!</h1>
            <Container>
            <TableWrapper color="whitesmoke">
                <Table striped bordered hover>
                    <thead>
                    <tr>
                        <th>Temprature</th>
                        <th>Sugar Level</th>
                        <th>BP Level</th>
                        <th>Advice</th>
                        <th>Prescription</th>
                        <th>Confirmed Diseases</th>
                    </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{prescription.temprature}</td>
                            <td>{prescription.sugar_level}</td>
                            <td>{prescription.bp_level}</td>
                            <td>{prescription.Advice}</td>
                            <td>{prescription.prescription}</td>
                            <td>{prescription.confirmed_diseases}</td>
                        </tr>
                    </tbody>
                </Table>
            </TableWrapper>
            {/* Need Go back and Check Previous Checkup Buttons Here */}
            </Container>
        </div>
    )
}
