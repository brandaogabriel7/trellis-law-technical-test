import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

type GetEnglishNumberResponse = {
  status: string;
  num_in_english: string | undefined;
  error: string | undefined;
};

export const getEnglishNumber = async (
  number: number
): Promise<GetEnglishNumberResponse> => {
  const response = await axios.get(
    `${API_BASE_URL}/num_in_english/?number=${number}`
  );
  return response.data;
};

export const postEnglishNumber = async (
  number: number
): Promise<GetEnglishNumberResponse> => {
  const response = await axios.post(`${API_BASE_URL}/num_in_english/`, {
    number,
  });
  return response.data;
};
