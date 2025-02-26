<script setup lang="ts">
const { title, message, type, compact } = defineProps<{
  compact?: boolean;
  type: 'success' | 'error';
  title: string;
  message: string | null;
}>();
</script>

<template>
  <div
    :class="{
      'card shadow-lg': true,
      compact: compact,
      'bg-green-100 text-green-800': type === 'success',
      'bg-red-100 text-red-800': type === 'error',
    }"
  >
    <div class="card-body">
      <h2 class="card-title">{{ title }}</h2>
      <p>{{ message }}</p>
    </div>
  </div>
</template>
