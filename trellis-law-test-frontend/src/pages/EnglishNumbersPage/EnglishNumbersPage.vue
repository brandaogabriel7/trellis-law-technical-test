<script setup lang="ts">
import { ref } from 'vue';
import { getEnglishNumber, postEnglishNumber } from '../../services/api';
import { AxiosError } from 'axios';
import EnglishNumbersResult from './components/EnglishNumbersResult/EnglishNumbersResult.vue';
import Loading from '../../components/Loading/Loading.vue';
import EnglishNumbersRequestForm from './components/EnglishNumbersRequestForm/EnglishNumbersRequestForm.vue';

const loading = ref<boolean>(false);
const result = ref<string | null>(null);
const error = ref<string | null>(null);

const onSubmit = async (number: number, method: 'get' | 'post') => {
  if (number === null || method === null) {
    return;
  }

  loading.value = true;

  const englishNumberFunction =
    method === 'get' ? getEnglishNumber : postEnglishNumber;
  try {
    const response = await englishNumberFunction(number);
    if (response.status === 'ok' && response.num_in_english) {
      result.value = response.num_in_english;
      error.value = null;
    }
    if (response.status === 'error' && response.error) {
      error.value = response.error;
      result.value = null;
    }
  } catch (err) {
    result.value = null;
    if (err instanceof AxiosError && err?.response?.data?.status === 'error') {
      error.value = err.response?.data?.error;
    }
    error.value = error.value
      ? error.value
      : 'An unexpected error occurred. Try again later';
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="container mx-auto p-4 flex flex-col items-center md:w-1/2">
    <main class="w-full">
      <h1 class="text-3xl font-bold mb-4 text-center">English numbers</h1>
      <EnglishNumbersRequestForm @submit="onSubmit" />
    </main>
    <section class="w-full mt-4">
      <EnglishNumbersResult
        :loading="loading"
        :result="result"
        :error="error"
      />
    </section>
  </div>
  <Loading :is-loading="loading" />
</template>
