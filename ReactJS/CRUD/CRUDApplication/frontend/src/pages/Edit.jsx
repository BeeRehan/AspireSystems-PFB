import {Button,Form,FloatingLabel,} from 'react-bootstrap'
import {React,useState,useEffect} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import {useNavigate, useParams} from 'react-router-dom'


export default function Edit() {

    const {id} = useParams()
    const [details,setDetails] = useState({});
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
          'name':data.name,
          'age':data.age,
          'occupation':data.occupation
        })
      })
    }, [id])
  
  
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