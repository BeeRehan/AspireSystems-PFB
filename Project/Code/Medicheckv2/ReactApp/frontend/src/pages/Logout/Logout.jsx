import React from 'react'
import Cookies from 'universal-cookie';
import { useNavigate,Navigate} from  "react-router-dom";

export default function Logout() {
    const navigate = useNavigate();
    const cookies = new Cookies();
    cookies.remove('jwt');
    navigate("/login");
    return (
        <div>
            <h1>Come back soon</h1>
        </div>
    )
}
