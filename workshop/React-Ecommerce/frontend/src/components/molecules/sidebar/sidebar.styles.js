import styled from 'styled-components'

export const sideBarWrapper = styled.div`  
  .nav-menu {
    background-color: ${(props)=>props.bgcolor||"#fff"};
    width: 250px;
    height: 100vh;
    position: fixed;
    top: 0;
    left: -100%;
    z-index: 2;
    transition: 850ms;
  }
  
  .nav-menu.active {
    left: 0;
    transition: 350ms;
  }
  .nav-text{
    margin  : 2px;
    border-radius : 50%;
  }
  .nav-text a{
    text-decoration : none;
    color : #fff;
  }
`;