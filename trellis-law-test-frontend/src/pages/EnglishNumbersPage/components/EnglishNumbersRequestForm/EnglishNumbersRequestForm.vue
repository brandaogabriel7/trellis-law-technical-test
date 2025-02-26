<script setup lang="ts">
import { ref } from 'vue';

const emit = defineEmits<{
  submit: [number: number, method: 'get' | 'post'];
}>();
const number = ref<number | null>(null);
const method = ref<'get' | 'post'>('get');

const onSubmit = () => {
  if (number.value !== null && method.value !== null) {
    emit('submit', number.value, method.value);
  }
};
</script>
<template>
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
      <label class="label cursor-pointer flex justify-start">
        <input
          v-model="method"
          type="radio"
          name="method"
          value="get"
          class="radio radio-primary"
        />
        <span class="label-text ml-2">GET</span>
      </label>
      <label class="label cursor-pointer flex justify-start">
        <input
          v-model="method"
          type="radio"
          name="method"
          value="post"
          class="radio radio-primary"
        />
        <span class="label-text ml-2">POST</span>
      </label>
    </div>
    <button class="btn btn-primary w-full" type="submit">Submit</button>
  </form>
</template>
