<script setup lang="ts">
const { loading, result, error } = defineProps<{
  loading: boolean;
  result: string | null;
  error: string | null;
}>();
</script>
<template>
  <div class="mt-4">
    <div
      v-if="!loading && result"
      class="card bg-green-100 text-green-800 shadow-lg p-4"
    >
      <div class="card-body">
        <h2 class="card-title">Result</h2>
        <p>{{ result }}</p>
      </div>
    </div>
    <div
      v-if="!loading && error"
      class="card bg-red-100 text-red-800 shadow-lg p-4"
    >
      <div class="card-body">
        <h2 class="card-title">Error</h2>
        <p>{{ error }}</p>
      </div>
    </div>
  </div>
</template>
