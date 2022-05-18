import React,{ useState } from 'react'
import * as S from './headers.styles'
import { Link } from 'react-router-dom'
import Logo from "components/atoms/logo/index"
import SideBar from 'components/molecules/sidebar/index'
import { Badge } from 'react-bootstrap'
import { UserService } from 'core/user.service'
import { AuthService } from 'core/auth.service'
import { toast } from 'react-toastify';

export default function Header(props) {
  const [showBar, setShowBar] = useState(false);
  let isLogin = UserService.accessToken || false;

  function signout(){
    AuthService.clearStorage();
    toast.success("See you soon!!!")
    window.location.replace("/");
  }

  return (
    <S.HeaderNav>
        <SideBar show={showBar}/>
        <Link to="/">
          <Logo width={'55px'}/>
        </Link>
        <h1>MD</h1>
        <S.NavItem>
          <Link to="/cart">
            Cart  <Badge pill bg="danger">{props.cartTotal}
        </Badge>{' '}
          </Link>
          <Link to="/about">
            About
          </Link>
          {!isLogin &&
          <>
            <Link to="/signin">
              SignIn
            </Link>
            <Link to="/signup">
              SignUp
            </Link>
          </>
          }
          {isLogin   &&
          <>
            <Link onClick={signout} to="/">
              SignOut
            </Link>
          </>
          }
          <Link to={""} onClick={()=>setShowBar(!showBar)}>III</Link>
        </S.NavItem>
    </S.HeaderNav>
  )
}
