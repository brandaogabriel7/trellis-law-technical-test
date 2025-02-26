<script setup lang="ts">
const number = defineModel();
const { label, inputId, placeholder, ...props } = defineProps<{
  inputId?: string;
  label: string;
  placeholder: string;
}>();
</script>
<template>
  <div class="form-control">
    <label :for="inputId" class="label">{{ label }}</label>
    <input
      :id="inputId"
      v-bind="props"
      v-model="number"
      type="number"
      class="input input-bordered w-full"
    />
  </div>
</template>
