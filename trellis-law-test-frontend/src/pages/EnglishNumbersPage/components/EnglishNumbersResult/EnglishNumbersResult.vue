<script setup lang="ts">
import ResultsCard from './ResultsCard.vue';

const { loading, result, error } = defineProps<{
  loading: boolean;
  result: string | null;
  error: string | null;
}>();
</script>
<template>
  <div class="mt-4">
    <ResultsCard
      v-if="(!loading && result) || (!loading && error)"
      :type="result ? 'success' : 'error'"
      :message="result || error"
    />
  </div>
</template>
