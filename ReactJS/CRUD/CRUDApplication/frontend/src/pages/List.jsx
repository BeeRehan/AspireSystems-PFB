import {Button,Table,Container} from 'react-bootstrap'
import {React,useState,useEffect} from 'react'
import {Link} from 'react-router-dom'

import Skeleton from '@material-ui/lab/Skeleton';

export default function List() {
    const [users, setUsers] = useState(null);
    function fetchData(){
      fetch('http://localhost:8000/api/rest-list/')
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
        setTimeout(() => {
          setUsers(data)
        }, 2021);
      })
      .catch(er=>{
        console.log("Error in List",er);
      })
    }
  
    useEffect(() => {
      fetchData()
    },[])
  
    function toDelete(id){
      console.log("Deleted");
      fetch(`http://localhost:8000/api/rest-delete/${id}`,{
        method:"DELETE"
      })
      .then(res=>{
        if(res.ok){
          fetchData()
          // window.location.reload()
        }
        throw res
      })
      .catch(er=>{
        console.log("Error in List",er);
      })
      
    }
    console.log("user",users)
    if(users){
      return (
        <Container>
          <Table striped bordered hover>
          <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>Occupation</th>
                <th>To Edit</th>
                <th>To Delete</th>
            </tr>
            </thead>
            <tbody>
              {
                users.map((user)=>{
                  return(
                    <tr key={user.id}>
                    <td>{user.name}</td>
                    <td>{user.age}</td>
                    <td>{user.occupation}</td>
                    <td><Link to={`/edit/${user.id}`}>Edit</Link></td>
                    <td><Button onClick={()=>toDelete(user.id)}>Delete</Button></td>
                    </tr>
                  );
                })
              }
            </tbody>
          </Table>
          <Button as={Link} to={'/'}>Add new </Button>
        </Container>
      ) 
    }
    else{
      return(
        <Container>
        <Table striped bordered hover>
        <thead>
          <tr>
              <th>Name</th>
              <th>Age</th>
              <th>Occupation</th>
              <th>To Edit</th>
              <th>To Delete</th>
          </tr>
          </thead>
          <tbody>
            {
              [1,2,3].map((user)=>{
                return(
                  <tr key={user}>
                  <td><Skeleton /></td>
                  <td><Skeleton animation="wave" /></td>
                  <td><Skeleton animation="wave" /></td>
                  <td><Skeleton animation="wave" /></td>
                  <td><Skeleton animation="false" /></td>
                  </tr>
                );
              })
            }
          </tbody>
        </Table>
        <Button as={Link} to={'/'}>Add new </Button>
      </Container>
        
      );
    }
  }