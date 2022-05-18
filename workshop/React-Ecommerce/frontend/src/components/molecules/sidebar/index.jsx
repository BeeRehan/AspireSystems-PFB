import React from "react";
import { Link } from "react-router-dom";
import barData from "./sidebarData"
import * as S from "./sidebar.styles"
import { Button } from "react-bootstrap";

export default function SideBar ({show}){
    return (
        <S.sideBarWrapper>
            <nav className={show ? 'nav-menu active' : 'nav-menu'}>
            <h1>Who are we?</h1>
            <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Delectus assumenda quas explicabo sequi, labore tempore iste velit dolor quia aliquid molestias inventore corrupti, libero minima voluptas accusamus cumque, maiores totam?</p>
            {barData.map((item, index) => {
              return (
                <Button key={index} className={item.cName}>
                  <Link to={item.path}>
                    {item.title}
                  </Link>
                </Button>
              );
            })}
            </nav>
        </S.sideBarWrapper>
        );
  };