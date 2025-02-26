<script setup lang="ts">
import MessageCard from '../../../../components/MessageCard/MessageCard.vue';

const { loading, result, error } = defineProps<{
  loading: boolean;
  result: string | null;
  error: string | null;
}>();
</script>
<template>
  <div class="mt-4">
    <MessageCard
      v-if="(!loading && result) || (!loading && error)"
      :type="result ? 'success' : 'error'"
      :message="result || error"
      compact
    />
  </div>
</template>
