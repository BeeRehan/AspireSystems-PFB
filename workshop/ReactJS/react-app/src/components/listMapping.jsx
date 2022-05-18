import React from "react";
import { BrowserRouter } from "react-router-dom";

export default function ListItem(){
   const arr = ['car','car','car','car'];

    const lii = arr.map(item=><li>{item}</li>);
    console.log(lii);
    return(
        <ul>
            {lii}
        </ul>
    )
}