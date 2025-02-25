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
    }
    if (response.status === 'error' && response.error) {
      error.value = response.error;
    }
  } catch (err) {
    if (err instanceof AxiosError) {
      error.value =
        err.response?.data.error || err.message || 'An error occurred';
    } else {
      error.value = 'An error occurred';
    }
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <main class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">English numbers</h1>
    <EnglishNumbersRequestForm @submit="onSubmit" />
  </main>
  <aside>
    <EnglishNumbersResult :loading="loading" :result="result" :error="error" />
  </aside>
  <Loading :is-loading="loading" />
</template>
