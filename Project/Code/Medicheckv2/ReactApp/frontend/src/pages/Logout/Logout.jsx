import {React,useEffect} from 'react'
import Cookies from 'universal-cookie';
import { useNavigate,Navigate} from  "react-router-dom";

export default function Logout() {
    const navigate = useNavigate();
    const cookies = new Cookies();
    useEffect(() => {
        cookies.remove('jwt');
        navigate("/login")
        window.location.reload()
    }, [])
   
    return (
        <div>
            <h1>Come back soon{ navigate("/login")}</h1>
        </div>
    )
}
