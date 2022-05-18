import './App.css';
import ComponentOne from './components/componentOne';
import ComponentTwo from './components/componentTwo';
import { Provider } from 'react-redux'
import store from './redux/store';

function App() {
  return (
    <Provider store={store}>
      <div className="App">
        <ComponentOne/>
        <ComponentTwo/>
      </div>
    </Provider>
  );
}

export default App;
