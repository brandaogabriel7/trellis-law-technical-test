import HelloWorld from '../HelloWorld.vue';
import { render, screen } from '@testing-library/vue';

describe('Hello World', () => {
  it('renders hello world', () => {
    render(HelloWorld);

    expect(screen.getByText(/hello world/i)).toBeInTheDocument();
  });
});
