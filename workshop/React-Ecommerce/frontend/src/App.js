import { useState } from "react";
import HomePage from "components/organisms/homepage/index";
import SignIn from "components/organisms/signin";
import SignUp from "components/organisms/signup";
import { BrowserRouter as Router, Routes,Route } from "react-router-dom";
import Cart from "components/organisms/cart";

function App() {
  const [cart, setCart] = useState([])

  const handleAddCart = (item)=>{
    let flag = true

   cart.forEach((itm,ind)=>{
      if(itm.title===item.title){
        flag = false
      }
   })
   if(flag){
     setCart([...cart, item]);
   }
  }
  const handleChange = (item, d) => {
    let index;
    cart.forEach((itm,ind)=>{
       if(itm.title===item.title){
         index=ind;
       } 
    })
    let arr,obj;
    arr = cart;
    obj = Object.assign({},arr[index])
    obj.quantity +=d;
    arr[index] = obj;
    setCart([...arr]);
  };

  const handleRemove = (title) =>{
    const arr = cart.filter((item,ind)=>item.title!==title)
    setCart([...arr])
  }
  
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomePage addCart={handleAddCart} cartTotal={cart.length}/>}/>
          <Route path="/signin" element={<SignIn/>}/>
          <Route path="/signup" element={<SignUp/>}/>
          <Route path="/about" element={<h1>Under Construction!!!</h1>}/>
          <Route path="/cart" element={<Cart changeQuantity={handleChange} removeItem={handleRemove} items={cart}/>}/>
        </Routes>
      </Router>  
    </div>
  );
}

export default App;
