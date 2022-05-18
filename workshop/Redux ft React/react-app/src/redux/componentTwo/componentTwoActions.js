import { TO_INCREASE } from './componentTwoActionTypes'

export const increase = (value = 1)=>{
    return {
        type : TO_INCREASE,
        pay_load: Number(value),
    }
}