import {React,useState,useEffect} from 'react'
import {Table,Container,Button} from 'react-bootstrap'
import {useNavigate} from 'react-router-dom'
import {TableWrapper} from '../../static/css/styledcompunent/StyleCompounent'
import Navbar from '../../components/universe/Navbar'
import Cookies from 'universal-cookie'

const cookies = new Cookies();
export default function Admin() {
    const [users, setUsers] = useState([]);
    const navigate = useNavigate()

    function fetchUsers(){
        fetch('http://localhost:8000/users/api/list_users',{
          method:"GET",
          headers:{
            'Content-Type':"application/json",
            "Authorization":cookies.get('jwt')['jwt'],
          },
      })
      .then(res=>{
        if(res.ok){
          return(
            res.json()
          ); 
        }
        throw res
      })
      .then(data=>{
        // console.log("DataR",data)
        setUsers(data)
      })
      .catch(er=>{
        console.log("Error in List",er);
      })
    }
    useEffect(() => {
        fetchUsers();
    },[])
  
    function toDelete(id){
      console.log("Deleted",id)
      fetch(`http://localhost:8000/users/api/delete_data/${id}`,{
        method:"DELETE"
      })
      .then(res=>{
        if(res.ok){
            fetchUsers();
        }
        throw res
      })
      .catch(er=>{
        console.log("Error in List",er);
      })
      
    }
  
    return (
    <>
    <Navbar  name="Add users" link="/admins/add_users"/>
      <Container>
        <TableWrapper color="whitesmoke">
        <Table striped bordered hover>
        <thead>
          <tr>
              <th>User ID</th>
              <th>Name</th>
              <th>Group</th>
              <th>Status</th>
              <th>Action</th>
          </tr>
          </thead>
          <tbody>
            {
              users.map((user)=>{
                return(
                  <tr key={user.id}>
                  <td>{user.id}</td>
                  <td>{user.username}</td>
                  <td>{user.group}</td>
                  <td>{user.status}</td>
                  <td><Button onClick={()=>toDelete(user.id)}>Delete</Button></td>
                  </tr>
                );
              })
            }
          </tbody>
        </Table>
        </TableWrapper>
      </Container>
    
    </>
    )
}
