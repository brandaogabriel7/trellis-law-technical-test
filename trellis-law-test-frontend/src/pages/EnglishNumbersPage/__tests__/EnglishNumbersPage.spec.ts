import { render, screen } from '@testing-library/vue';
import EnglishNumbersPage from '../EnglishNumbersPage.vue';

describe('EnglishNumbersPage', () => {
  it('should render', () => {
    render(EnglishNumbersPage);
    expect(screen.getByText(/english numbers/i)).toBeInTheDocument();
  });
});
