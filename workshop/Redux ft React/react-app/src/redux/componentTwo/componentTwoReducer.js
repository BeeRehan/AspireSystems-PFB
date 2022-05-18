import { TO_INCREASE } from './componentTwoActionTypes'

const intialState = {
    count : 10
}

const secondReducer = (state=intialState,action)=>{
    switch(action.type){
        case TO_INCREASE:{
            return{
                ...state,
                count:state.count + action.pay_load
            }
        }
        default:{
            return state;
        }
    }
}

export default secondReducer;


