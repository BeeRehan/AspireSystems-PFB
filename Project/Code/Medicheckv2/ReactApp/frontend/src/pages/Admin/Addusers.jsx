import {React,useState} from 'react'
import Input from '../../components/atoms/Input/Input.jsx'
import Buton from '../../components/atoms/Button/Button.jsx'
import {inputs,selectGroup,selectGender} from "./config.js"
import Cookies from 'universal-cookie'
import SelectInput from '../../components/atoms/Input/SelectInput'
import { useNavigate } from 'react-router-dom'
import {Wrapper} from '../../static/css/styledcompunent/StyleCompounent.js'
import { Form,FloatingLabel } from 'react-bootstrap';

import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';

const schema = yup.object().shape({
    Username: yup.string().required("Enter the Username!!!"),
    Password: yup.string().required("Enter the password!!!").min(8).max(24),
    Age: yup.number().required("Enter the age!!!").positive().integer(),
    ["Secret Key"]: yup.string().required("Enter the secret key!!!"),
}).required();


const cookies = new Cookies()
export default function Addusers() {
    const [userDetails, setUserDetails] = useState({});
    const navigate = useNavigate();

    const { register, handleSubmit, watch,formState: { errors } } = useForm({
        resolver: yupResolver(schema),
      });
    
    const handler = (e)=>{
        console.log([e.target.name],e.target.value,":",watch(e.target.name))
        setUserDetails(prevstate=>{
            return{
                ...prevstate,
                [e.target.name]:e.target.value}});
            };
    
        
    function submit(data){
        console.log("Details:",{...userDetails,...data})
        fetch('http://127.0.0.1:8000/users/api/add_user',{
        method:"POST",
        headers : {
            'Content-Type':"application/json",
            "Authorization":cookies.get('jwt')['jwt'],
        },
        body  : JSON.stringify({...userDetails,...data}),
        })
        .then(res=>{
            if(res.ok){
                return res.json()
            }
            throw res
        })
        .then(data=>{
            console.log("Data",data);
            navigate('/admins')
        })
        .catch(er=>{
            console.log("Error:",er)
        })
        return false;
    }

    return (
        <div>
            <form className="form" onSubmit={handleSubmit(submit)}>
                <h1>My Profile</h1>
                {
                    inputs.map((input)=>{
                        return(
                            <div key={input.label}>
                                <FloatingLabel controlId={input.label} className="mb-2" label={input.label}>
                                    <Form.Control type={input.type} name={input.label} placeholder={input.placeholder} onChange={(e)=>handler(e)} {...register(input.label, { required: true })}/>
                                </FloatingLabel>
                                <span>{errors[input.label]?.message}</span>
                            </div>
                                          
                        );
                    })
                }
                <SelectInput label="Group" name="Group" onChange={(e)=>handler(e)} option={selectGroup}/>
                <SelectInput label="Gender" name="Gender" onChange={(e)=>handler(e)} option={selectGender}/>
                <Wrapper><Buton type="submit" variant="primary" name="Submit"/></Wrapper>
            </form>
        </div>
    )
}
