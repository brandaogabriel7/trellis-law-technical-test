<script setup lang="ts">
import FormNumberInputProps from './FormNumberInputProps';

const number = defineModel();
const { label, placeholder, ...props } = defineProps<FormNumberInputProps>();
</script>
<template>
  <div class="form-control">
    <label class="label">
      <input
        v-bind="props"
        v-model="number"
        type="number"
        class="input input-bordered w-full"
      />
      <span class="label-text">{{ label }}</span>
    </label>
  </div>
</template>
