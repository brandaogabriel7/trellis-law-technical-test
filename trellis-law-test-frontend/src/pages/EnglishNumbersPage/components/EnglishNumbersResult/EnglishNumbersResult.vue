<script setup lang="ts">
import MessageCard from '../../../../components/MessageCard/MessageCard.vue';
import EnglishNumbersResultProps from './EnglishNumbersResultProps';

const { loading, result, error } = defineProps<EnglishNumbersResultProps>();
</script>
<template>
  <div class="mt-4">
    <MessageCard
      v-if="(!loading && result) || (!loading && error)"
      :type="result ? 'success' : 'error'"
      :title="result ? 'Result' : 'Error'"
      :message="result || error"
      compact
    />
  </div>
</template>
