<script setup lang="ts">
import { ref } from 'vue';
import FormNumberInput from './FormNumberInput.vue';
import FormMethodInput from './FormMethodInput.vue';

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
    <FormNumberInput v-model="number" />
    <FormMethodInput v-model="method" />
    <button class="btn btn-primary w-full" type="submit">Submit</button>
  </form>
</template>
