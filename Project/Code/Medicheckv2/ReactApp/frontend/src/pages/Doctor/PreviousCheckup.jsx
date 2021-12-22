import {React,useState,useEffect} from 'react'
import { Container,Table } from 'react-bootstrap'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'
import Cookies from 'universal-cookie'
import {useParams,useNavigate, Link} from 'react-router-dom'

const cookies = new Cookies();
export default function PreviousCheckup() {
    const [list, setList] = useState([{}]);
    const {pid} = useParams();

    function fetchPreviousCheckup(){
        fetch(`http://127.0.0.1:8000/checkup/api/prev_checklist/${pid}`,{
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
            setList(data)
        }).catch(err=>{
            console.log(err);
        })
    }

    useEffect(()=>{
        console.log("fetching........")
        fetchPreviousCheckup();
    },[]);

    console.log("HelloL",list)
    return (
        <div>
            <h1>Previous Checkups!!!</h1>
            <Container>
            <TableWrapper color="whitesmoke">
                <Table striped bordered hover>
                    <thead>
                    <tr>
                        <th>Appoinment ID</th>
                        <th>Appoinment</th>
                        <th>To check</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        list.map((listItem)=>{
                            return(
                                <tr>
                                    <td>{listItem.id}</td>
                                    <td>{listItem.date}</td>
                                    <td><Link to={`/doctors/checklist/userdetails/checkupupdetails/${listItem.id}`}>For Details</Link></td>
                                </tr>
                            );
                        })
                    }
                    </tbody>
                </Table>
            </TableWrapper>
            {/* Need Goback Button Here */}
            </Container>
        </div>
    )
}
