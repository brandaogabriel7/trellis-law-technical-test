<script setup lang="ts">
import { ref } from 'vue';
import FormMethodInput from '../FormMethodInput/FormMethodInput.vue';
import FormNumberInput from '../../../../components/FormNumberInput/FormNumberInput.vue';
import EnglishNumbersRequestFormEmits from './EnglishNumbersRequestFormEmits';

const emit = defineEmits<EnglishNumbersRequestFormEmits>();
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
    <FormNumberInput
      v-model="number"
      id="number-input"
      name="number"
      label="Number:"
      placeholder="Enter a number"
      :min="0"
      :max="999999999999999"
      required
    />
    <FormMethodInput v-model="method" />
    <button class="btn btn-primary w-full" type="submit">Submit</button>
  </form>
</template>
