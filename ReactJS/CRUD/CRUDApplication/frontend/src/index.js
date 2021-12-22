import {Button,Form,FloatingLabel,Table,Container} from 'react-bootstrap'
import {React,useState,StrictMode,useEffect} from 'react'
import ReactDOM from 'react-dom';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter as Router, Routes,Route,useNavigate, Link,useParams} from 'react-router-dom'
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';

const schema = yup.object().shape({
    name: yup.string().required(),
    age: yup.string().required().min(8).max(24),
    occupation: yup.number().required().positive().integer(),

}).required();


ReactDOM.render(
  <StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/list" element={<List/>} />
        <Route path="/edit/:id" element={<Edit/>} />
      </Routes>
    </Router>
  </StrictMode>,
  document.getElementById('root')
);

reportWebVitals();

function Home() {

  const [details,setDetails] = useState({});
  const navigate = useNavigate();

  
  const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: yupResolver(schema),
  });

  function handler(e){
    setDetails((prev)=>{
    return{
      ...prev,
    [e.target.name] : e.target.value      
    };
      
    })
  }

  function submit(e){
    e.preventDefault();
    console.log(details)
    fetch('http://localhost:8000/api/rest-create/',{
      method:"POST",
      headers:{
        "Content-type":"application/json",
      },
      body:JSON.stringify(details)
    }).then((res)=>{
      if(res.ok){
        console.log("Pushed");
        navigate("/list")
      }
    }).catch(er=>{
      console.log("Error:",er);
    })
  }
  return (
    <div>
      <form className="form" onSubmit={handleSubmit(submit)}>
        {console.log("ErrorsObj:",errors,"Register",register)}
        <FloatingLabel controlId="floatingInputName"  label="Name" className="mb-3">
          <Form.Control type="text" placeholder="name" {...register('name', { required: true })} name="name" value={details.name} onChange={handler} required/>
          <span>{errors.name?.message}</span>
        </FloatingLabel>
        <FloatingLabel controlId="floatingInputAge" label="Age" className="mb-3">
          <Form.Control type="number" placeholder="age" {...register('age', { required: true })} name="age" value={details.age} onChange={handler} required/>
          <span>{errors.age?.message}</span>
        </FloatingLabel>
        <FloatingLabel controlId="floatingInputOccupation" label="Occupation" className="mb-3">
          <Form.Control type="text" placeholder="occupation" {...register('occupation', { required: true })} name="occupation" value={details.ooccupation} onChange={handler} required/>
          <span>{errors.occupation?.message}</span>
        </FloatingLabel>
        <Button type="submit">Submit</Button>
      </form>
    </div>
  )
}


function List() {
  const [users, setUsers] = useState([]);
  const navigate = useNavigate()
  
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
      setUsers(data)
    })
    .catch(er=>{
      console.log("Error in List",er);
    })
  }

  useEffect(() => {
    fetchData()
  },users)

  function toDelete(id){
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
                <td><Button onClick={toDelete(user.id)}>Delete</Button></td>
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


function Edit() {

  const {id} = useParams()
  const [details,setDetails] = useState({
    'name':"",
    'age' : "",
    'occupation':""
  });
  const navigate = useNavigate();
  
  useEffect(() => {
    fetch(`http://localhost:8000/api/rest-get/${id}/`,{
      method:"GET"
    })
    .then(res=>{
      if(res.ok){
        return(
          res.json()
        );
      }
      throw res;
    })
    .then(data=>{
      console.log(data)
      setDetails({
        ...details,
        ['name']:data.name,
        ['age']:data.age,
        ['occupation']:data.occupation
      })
    })
  }, [])


  function handler(e){
    setDetails((prev)=>{
    return{
      ...prev,
    [e.target.name] : e.target.value      
    };
      
    })

  }

  function submit(e){
    e.preventDefault();
    console.log(details)
    fetch(`http://localhost:8000/api/rest-update/${id}/`,{
      method:"POST",
      headers:{
        "Content-type":"application/json",
      },
      body:JSON.stringify(details)
    }).then((res)=>{
      if(res.ok){
        console.log("Pushed");
        navigate("/list")
      }
    }).catch(er=>{
      console.log("Error:",er);
    })
  }

  return (
    <div>
      <form className="form" onSubmit={submit}>
        <FloatingLabel controlId="floatingInputName"  label="Name" className="mb-3">
          <Form.Control type="text" placeholder="name" name="name" value={details.name} onChange={handler} required/>
        </FloatingLabel>
        <FloatingLabel controlId="floatingInputAge" label="Age" className="mb-3">
          <Form.Control type="number" placeholder="age" name="age" value={details.age} onChange={handler} required/>
        </FloatingLabel>
        <FloatingLabel controlId="floatingInputOccupation" label="Occupation" className="mb-3">
          <Form.Control type="text" placeholder="occupation" name="occupation" value={details.occupation} onChange={handler} required/>
        </FloatingLabel>
        <Button type="submit">Submit</Button>
      </form>
    </div>
  )
}