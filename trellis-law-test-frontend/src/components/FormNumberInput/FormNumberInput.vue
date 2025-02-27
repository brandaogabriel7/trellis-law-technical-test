<script setup lang="ts">
import FormNumberInputProps from './FormNumberInputProps';

const number = defineModel();
const {
  id = 'my-default-number-input-id',
  label,
  ...props
} = defineProps<FormNumberInputProps>();
</script>
<template>
  <div class="form-control">
    <label :for="id" class="label">{{ label }}</label>
    <input
      :id="id"
      v-bind="props"
      v-model="number"
      type="number"
      class="input input-bordered w-full"
    />
  </div>
</template>
