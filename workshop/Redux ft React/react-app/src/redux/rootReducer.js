import { combineReducers } from 'redux'
import secondReducer from './componentTwo/componentTwoReducer'
import firstReducer from './componentOne/componentOneReducer'

const rootReducer = combineReducers({
    first: firstReducer,
    second: secondReducer
})

export default rootReducer;