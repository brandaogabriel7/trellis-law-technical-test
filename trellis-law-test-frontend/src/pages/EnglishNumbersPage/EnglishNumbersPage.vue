<script setup lang="ts">
import { ref } from 'vue';
import { getEnglishNumber, postEnglishNumber } from '../../services/api';
import { AxiosError } from 'axios';

const number = ref<number | null>(0);
const method = ref<'get' | 'post' | null>('get');
const loading = ref<boolean>(false);
const result = ref<string | null>(null);
const error = ref<string | null>(null);

const onSubmit = async () => {
  if (number.value === null || method.value === null) {
    return;
  }

  loading.value = true;

  const englishNumberFunction =
    method.value === 'get' ? getEnglishNumber : postEnglishNumber;
  try {
    const response = await englishNumberFunction(number.value);
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
    <form @submit.prevent="onSubmit" class="space-y-4">
      <div class="form-control">
        <label for="number-input" class="label">Number:</label>
        <input
          id="number-input"
          v-model="number"
          type="number"
          name="number"
          min="0"
          max="999999999999999"
          required
          placeholder="Enter a number"
          class="input input-bordered w-full"
        />
      </div>
      <div class="form-control">
        <h4 class="label-text">Method:</h4>
        <label class="label cursor-pointer">
          <span class="label-text">GET</span>
          <input
            v-model="method"
            type="radio"
            name="method"
            value="get"
            class="radio radio-primary"
          />
        </label>
        <label class="label cursor-pointer">
          <span class="label-text">POST</span>
          <input
            v-model="method"
            type="radio"
            name="method"
            value="post"
            class="radio radio-primary"
          />
        </label>
      </div>
      <button class="btn btn-primary w-full" type="submit">Submit</button>
    </form>
  </main>
  <div class="mt-4">
    <p v-if="!loading && result" class="text-green-500">{{ result }}</p>
    <p v-if="!loading && error" class="text-red-500">{{ error }}</p>
  </div>
  <div
    v-if="loading"
    class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center z-50"
  >
    <span class="loading loading-spinner loading-lg text-white"
      >Loading...</span
    >
  </div>
</template>
