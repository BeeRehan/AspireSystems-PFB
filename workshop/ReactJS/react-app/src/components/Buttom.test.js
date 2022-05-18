import Buttom from "./Buttom";
import { render, screen } from '@testing-library/react';

test('renders learn react link', () => {
  render(<Buttom />);
  const linkElement = screen.getByText(/Buttom/i);
  expect(linkElement).toBeInTheDocument();
});
