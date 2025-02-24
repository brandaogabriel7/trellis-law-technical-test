<script setup lang="ts">
import { computed, ref } from 'vue';

const getEnglishNumber = () => {
  console.log('GET request');
};
const postEnglishNumber = () => {
  console.log('POST request');
};

const number = ref(0);
const method = ref('get');

const onSubmit = computed(() =>
  method.value === 'get' ? getEnglishNumber : postEnglishNumber
);
</script>

<template>
  <h1>English numbers</h1>
  <form @submit.prevent="onSubmit">
    <label for="number">Number:</label>
    <input
      v-model="number"
      type="number"
      name="number"
      min="0"
      max="999999999999999"
      required
      placeholder="Enter a number"
    />
    <label for="method">Method:</label>
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
</template>
