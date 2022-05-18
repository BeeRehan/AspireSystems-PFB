import React,{useState, useEffect} from 'react'
import Header from 'components/molecules/header/index'
import SubNav from 'components/molecules/subnavbar'
import Cards from 'components/atoms/cards/index'
import SkeletonLoder from 'components/atoms/skeleton/index'
import SideBar from 'components/molecules/sidebar/index'
import { UserService } from 'core/user.service'

export default function HomePage(props) {
  const [products,setProducts] = useState([]);
  const [loading, setLoading] = useState(false);
  useEffect(() => {
      UserService.listProduct()
      .then(res=>{
        setProducts(res);
        setLoading(true);
      })
  },[])
  const card = !loading? <SkeletonLoder/> : <Cards products={products} addCart={props.addCart}/>;
  return (
    <>
      <div>
        <Header cartTotal={props.cartTotal}/>
      </div>
      <div>
        <SubNav/>
      </div>
      <div>
        {card}
      </div>
      <div>
        <SideBar/>
      </div>
    </>
  )
}
