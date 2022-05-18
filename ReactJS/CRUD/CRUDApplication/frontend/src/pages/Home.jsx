import {Button,Form,FloatingLabel,} from 'react-bootstrap'
import {React,useState,useRef} from 'react'
import {useNavigate} from 'react-router-dom'
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import ReCAPTCHA from "react-google-recaptcha";

const schema = yup.object().shape({
    name: yup.string().required(),
    age: yup.number().required().positive().integer(),
    occupation: yup.string().required().min(8).max(24),

}).required();


export default function Home() {

  const [details,setDetails] = useState({});
  const navigate = useNavigate();
  const refCaptcha = useRef(null);
  
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

function validateCaptcha(){
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

  async function submit(e){
    console.log("Details:",details);
    const capToken = await refCaptcha.current.executeAsync();
    console.log("Token",capToken)
    refCaptcha.current.reset()
    const key = '6Lcg0cEdAAAAAFTNpNMC6C_z_J89wC7Ydav9DhUA'
    fetch(`https://www.google.com/recaptcha/api/siteverify?secret=${key}&response=${capToken}`,{
     method:'POST',
   }).then((res)=>{
     if(res.ok){
       return res.json()
     }
     return res
   }).then(res=>{
      if(res.success){
        validateCaptcha()
      }
   }).catch(err=>{
     console.log(err);
   })

    return false;
  }

  return (
    <div>
      <form className="form" onSubmit={handleSubmit(submit)}>
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
        <ReCAPTCHA ref={refCaptcha} sitekey="6Lcg0cEdAAAAABTc9I-jLzQ2SoE9243yMPxKOBtq" size='invisible'/>
        <Button type="submit">Submit</Button>
      </form>
    </div>
  )
}