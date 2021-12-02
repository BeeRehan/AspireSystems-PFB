import React from 'react'
import Cookies from 'universal-cookie';
import { useNavigate } from  "react-router-dom";

export default function Logout() {

const navigate = useNavigate();

    const cookies = new Cookies();
    cookies.remove('jwt');
    navigate("/");
    return (
        <div>
            <h1>Come back soon</h1>
        </div>
    )
}
