<script setup lang="ts">
const { isLoading } = defineProps<{
  isLoading: boolean;
}>();
</script>
<template>
  <div
    v-if="isLoading"
    class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center z-50"
  >
    <span class="loading loading-spinner loading-lg text-white"
      >Loading...</span
    >
  </div>
</template>
