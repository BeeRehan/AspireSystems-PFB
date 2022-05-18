import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Home from '../shop/Home';
import Contact from '../shop/contact';
import Items from '../shop/items';
import Nav from '../shop/Nav'
import MobileOprator from '../shop/mobileOprator'
import ItemDetails from '../shop/itemDetails'
import Buttom from "./Buttom";
import Label from "./label";

function App({name}) {
  
  return (
    <>
      <Router> 
      <Nav/>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/contact" element={<Contact/>}/>
          <Route path="/moperators" element={<MobileOprator/>}/>
          <Route path="shop" element={<Items/>}>
            {/* <Route index element={<main style={{ padding: "1rem" }}><p>Select an product</p></main>}/> */}
            <Route path=":name" element={<ItemDetails/>}/>
          </Route>
        </Routes>
      </Router>
      {/* <Buttom/>
      <Label/> */}
    </>
  );
}

export default App;
