import axios from 'axios';

type GetEnglishNumberResponse = {
  status: string;
  num_in_english: string | undefined;
  error: string | undefined;
};

export const getEnglishNumber = async (
  number: number
): Promise<GetEnglishNumberResponse> => {
  const response = await axios.get(
    `http://localhost:8000/num_in_english/?number=${number}`
  );
  return response.data;
};

export const postEnglishNumber = async (
  number: number
): Promise<GetEnglishNumberResponse> => {
  const response = await axios.post('http://localhost:8000/num_in_english/', {
    number,
  });
  return response.data;
};
