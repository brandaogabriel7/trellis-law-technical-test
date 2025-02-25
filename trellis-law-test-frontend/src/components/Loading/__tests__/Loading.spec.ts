import { render, screen } from '@testing-library/vue';
import Loading from '../Loading.vue';

describe('Loading', () => {
  it('should appear when loading', () => {
    render(Loading, {
      props: {
        isLoading: true,
      },
    });

    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });

  it('should not appear when not loading', () => {
    render(Loading, {
      props: {
        isLoading: false,
      },
    });

    expect(screen.queryByText(/loading/i)).not.toBeInTheDocument();
  });
});
