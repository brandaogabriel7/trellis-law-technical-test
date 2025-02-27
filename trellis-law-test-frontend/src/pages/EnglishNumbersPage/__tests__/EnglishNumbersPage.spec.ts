import { render, screen } from '@testing-library/vue';
import EnglishNumbersPage from '../EnglishNumbersPage.vue';
import userEvent from '@testing-library/user-event';
import { vi } from 'vitest';
import * as api from '../../../services/api';
import { AxiosError, AxiosRequestHeaders } from 'axios';

vi.mock('../../../services/api');

describe('EnglishNumbersPage', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });
  it('should render', () => {
    render(EnglishNumbersPage);

    expect(screen.getByText(/english numbers/i)).toBeInTheDocument();

    expect(
      screen.getByRole('spinbutton', { name: /number/i })
    ).toBeInTheDocument();

    expect(screen.getByRole('radio', { name: /get/i })).toBeInTheDocument();
    expect(screen.getByRole('radio', { name: /post/i })).toBeInTheDocument();

    expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument();
  });

  it.each([
    { number: 1, numInEnglish: 'one' },
    { number: 2, numInEnglish: 'two' },
    { number: 3, numInEnglish: 'three' },
    { number: 4, numInEnglish: 'four' },
    { number: 73, numInEnglish: 'seventy-three' },
    { number: 100, numInEnglish: 'one hundred' },
    { number: 101, numInEnglish: 'one hundred and one' },
    { number: 999, numInEnglish: 'nine hundred and ninety-nine' },
  ])(
    `should get number $number in english`,
    async ({ number, numInEnglish }) => {
      vi.spyOn(api, 'getEnglishNumber').mockResolvedValue({
        status: 'ok',
        num_in_english: numInEnglish,
        error: undefined,
      });
      const user = userEvent.setup();
      render(EnglishNumbersPage);

      const numberInput = screen.getByRole('spinbutton', { name: /number/i });
      expect(numberInput).toBeInTheDocument();

      await user.type(numberInput, number.toString());

      await user.click(screen.getByRole('radio', { name: /get/i }));

      await user.click(screen.getByRole('button', { name: /submit/i }));

      await screen.findByText(numInEnglish);
    }
  );

  it.each([
    { number: 1, numInEnglish: 'one' },
    { number: 4, numInEnglish: 'four' },
    { number: 73, numInEnglish: 'seventy-three' },
    { number: 101, numInEnglish: 'one hundred and one' },
    { number: 999, numInEnglish: 'nine hundred and ninety-nine' },
  ])(
    `should post number $number in english`,
    async ({ number, numInEnglish }) => {
      vi.spyOn(api, 'postEnglishNumber').mockImplementation(async () => {
        // delay to simulate network request
        await new Promise((resolve) => setTimeout(resolve, 10));
        return {
          status: 'ok',
          num_in_english: numInEnglish,
          error: undefined,
        };
      });
      const user = userEvent.setup();
      render(EnglishNumbersPage);

      const numberInput = screen.getByRole('spinbutton', { name: /number/i });
      expect(numberInput).toBeInTheDocument();

      await user.type(numberInput, number.toString());

      await user.click(screen.getByRole('radio', { name: /post/i }));

      await user.click(screen.getByRole('button', { name: /submit/i }));

      await screen.findByText(/loading/i);

      await screen.findByText(numInEnglish);
    }
  );

  it.each([
    { errorMessage: 'Number is too large', statusCode: 400 },
    { errorMessage: 'Number cannot be negative', statusCode: 400 },
    { errorMessage: 'Something went wrong', statusCode: 500 },
  ])(
    'should show error message $errorMessage. status: $statusCode',
    async ({ errorMessage, statusCode }) => {
      const error = new AxiosError();
      error.response = {
        status: statusCode,
        data: {
          status: 'error',
          error: errorMessage,
        },
        statusText: 'Internal Server Error',
        headers: {},
        config: {
          headers:
            (new AxiosError().response?.headers as AxiosRequestHeaders) || {},
        },
      };
      vi.spyOn(api, 'postEnglishNumber').mockRejectedValue(error);
      const user = userEvent.setup();
      render(EnglishNumbersPage);

      const numberInput = screen.getByRole('spinbutton', { name: /number/i });
      expect(numberInput).toBeInTheDocument();

      await user.type(numberInput, '99999999999');

      await user.click(screen.getByRole('radio', { name: /post/i }));

      await user.click(screen.getByRole('button', { name: /submit/i }));

      await screen.findByText(errorMessage);
    }
  );
});
