import React, { useState } from 'react'
import {useSelector,useDispatch} from 'react-redux'
import { increase } from '../redux/componentTwo/componentTwoActions'

export default function ComponentTwo(props){
  const count = useSelector((state)=>state.second.count)
  const dispatch = useDispatch()
  const [valuee,setValue] = useState(1);
  return (
    <div>
        componentTwo

        <h1>Counts: {count}</h1>
        <input type="text" value={valuee} onChange={(e)=>setValue(e.target.value)}/>
        <button onClick={()=>dispatch(increase(valuee))}>Increase{valuee}</button>
    </div>

  )
}
