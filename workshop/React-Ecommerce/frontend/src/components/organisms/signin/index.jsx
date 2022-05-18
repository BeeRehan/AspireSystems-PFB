import React from 'react'
import Header from 'components/molecules/header/index'
import * as S from './signin.styles'
import Field from 'components/molecules/fields/index'
import { useForm } from 'react-hook-form'
import { Button } from 'react-bootstrap'
import { EmailField,PasswordField } from "./constants"
import { UserService } from 'core/user.service'
import { AuthService } from 'core/auth.service'

export default function SignIn(props) {
  const {
    register,
    handleSubmit,
    formState : {errors},
  } = useForm();

  function onsubmit(values){
    UserService.signin(values)
    .then((res)=>{
      if(res && Object.keys(res).length){
        onSignSucess(res);
      }
    })
  }
  function onSignSucess(data){
    AuthService.setUser(data);
    window.location.replace("/");
  }
  return (
      <>
        <div>
            <Header/>
        </div>
        <div>
            <S.wrapper>
              <form onSubmit={handleSubmit(onsubmit)}>
                    {EmailField.map((obj,ind)=>(
                          <Field
                            key={ind}
                            {...obj}
                            register = { register }
                            error = { errors[obj.name]?.message }
                          />
                    ))
                    }
                    {PasswordField.map((obj,ind)=>(
                          <Field
                            key={ind}
                            {...obj}
                            register = { register }
                            error = { errors[obj.name]?.message }
                          />
                    ))
                    }
                    <S.Buttonwrapper>
                      <Button type='submit' style={{position:"relative",top:"10px",left:"15s0px"}}>Login</Button>
                    </S.Buttonwrapper>
              </form>
            </S.wrapper>
        </div>
      </>
  )
}
