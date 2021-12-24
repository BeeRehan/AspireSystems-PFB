import { render, screen } from '@testing-library/react';
import { shallow, mount } from "enzyme";
import toJSON from 'enzyme-to-json'
import Home from './pages/Home';
import List from './pages/List';

test('to test home compounent',()=>{
    render(<Home/>);
    const button = screen.getByRole('button', {
        name: /submit/i
      });
      expect(button).toBeInTheDocument();
})


it("renders without crashing", () => {
  const base = shallow(<Home />);
  const button = <h1>Add Here</h1>
  expect(base.contains(button)).not.toEqual(true);

});

it("renders correctly", () => {
  const tree = shallow(<Home/>);
  expect(toJSON(tree)).toMatchSnapshot();
});
