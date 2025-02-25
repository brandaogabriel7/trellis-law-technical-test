import axios from 'axios';

export const getEnglishNumber = async (
  number: number
): Promise<{
  status: string;
  num_in_english: string | undefined;
  error: string | undefined;
}> => {
  const response = await axios.get(
    `http://localhost:8000/num_in_english?number=${number}`
  );
  return response.data;
};

export const postEnglishNumber = async (
  number: number
): Promise<{
  status: string;
  num_in_english: string | undefined;
  error: string | undefined;
}> => {
  const response = await axios.post('http://localhost:8000/num_in_english', {
    number,
  });
  return response.data;
};
