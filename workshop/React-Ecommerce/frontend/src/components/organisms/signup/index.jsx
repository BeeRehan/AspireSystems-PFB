import React from 'react'
import Header from 'components/molecules/header/index'
import * as S from './signup.styles'
import Field from 'components/molecules/fields/index'
import { useForm } from 'react-hook-form'
import { Button } from 'react-bootstrap'
import { EmailField,PasswordField,RePasswordField,ageField,addressField } from "./constants"
import { UserService } from 'core/user.service'

export default function SignUp() {
    const {
        register,
        handleSubmit,
        formState : {errors},
        } = useForm();

    const onsubmit = (data)=>{
      UserService.siginup(data);
      // window.location.replace('/signin')
    }
  return (
    <div>
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
                    {RePasswordField.map((obj,ind)=>(
                          <Field
                            key={ind}
                            {...obj}
                            register = { register }
                            error = { errors[obj.name]?.message }
                          />
                    ))
                    }
                    {ageField.map((obj,ind)=>(
                          <Field
                            key={ind}
                            {...obj}
                            register = { register }
                            error = { errors[obj.name]?.message }
                          />
                    ))
                    }
                    {addressField.map((obj,ind)=>(
                          <Field
                            key={ind}
                            {...obj}
                            register = { register }
                            error = { errors[obj.name]?.message }
                          />
                    ))
                    }
                    <S.Buttonwrapper>
                        <Button type='submit' style={{position:"relative",top:"10px",left:"15s0px"}}>Register</Button>
                    </S.Buttonwrapper>
              </form>
            </S.wrapper>
        </div>
    </div>
  )
}
