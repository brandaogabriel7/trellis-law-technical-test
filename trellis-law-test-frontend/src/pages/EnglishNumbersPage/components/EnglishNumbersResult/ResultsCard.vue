<script setup lang="ts">
const { type, message } = defineProps<{
  type: 'success' | 'error';
  message: string | null;
}>();
</script>

<template>
  <div
    :class="{
      'card compact shadow-lg': true,
      'bg-green-100 text-green-800': type === 'success',
      'bg-red-100 text-red-800': type === 'error',
    }"
  >
    <div class="card-body">
      <h2 class="card-title">Result</h2>
      <p>{{ message }}</p>
    </div>
  </div>
</template>
