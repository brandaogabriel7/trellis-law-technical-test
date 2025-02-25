<script setup lang="ts">
import { ref } from 'vue';
import { getEnglishNumber, postEnglishNumber } from '../../services/api';

const number = ref<number | null>(0);
const method = ref<'get' | 'post' | null>('get');
const loading = ref<boolean>(false);
const result = ref<string | null>(null);

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
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <h1>English numbers</h1>
  <form @submit.prevent="onSubmit">
    <label for="number-input">Number:</label>
    <input
      id="number-input"
      v-model="number"
      type="number"
      name="number"
      min="0"
      max="999999999999999"
      required
      placeholder="Enter a number"
    />
    <h4>Method:</h4>
    <span>
      <input v-model="method" type="radio" id="get" name="method" value="get" />
      <label for="get">GET</label>
    </span>
    <span>
      <input
        v-model="method"
        type="radio"
        id="post"
        name="method"
        value="post"
      />
      <label for="post">POST</label>
    </span>
    <button type="submit">Submit</button>
  </form>
  <p v-if="loading">Loading...</p>
  <p v-if="!loading && result">{{ result }}</p>
</template>
