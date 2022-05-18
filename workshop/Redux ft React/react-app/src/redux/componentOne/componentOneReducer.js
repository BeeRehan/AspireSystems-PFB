import { TO_DCRECEASE } from './componentOneActionType'

const initialState = {
    count : 20
}

const firstReducer = (state = initialState,action)=>{
    switch(action.type){
        case TO_DCRECEASE:{
            return{
                ...state,
                count: state.count-1
            }
        }
        default:{
            return state;
        }
    }
}

export default firstReducer