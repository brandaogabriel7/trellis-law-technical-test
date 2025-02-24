import { render, screen } from '@testing-library/vue';
import EnglishNumbersPage from '../EnglishNumbersPage.vue';

describe('EnglishNumbersPage', () => {
  it('should render', () => {
    render(EnglishNumbersPage);

    expect(screen.getByText(/english numbers/i)).toBeInTheDocument();

    const numberInput = screen.getByPlaceholderText(/enter a number/i);
    expect(numberInput).toBeInTheDocument();
    expect(numberInput).toHaveAttribute('type', 'number');

    expect(screen.getByRole('radio', { name: /get/i })).toBeInTheDocument();
    expect(screen.getByRole('radio', { name: /post/i })).toBeInTheDocument();

    expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument();
  });
});
