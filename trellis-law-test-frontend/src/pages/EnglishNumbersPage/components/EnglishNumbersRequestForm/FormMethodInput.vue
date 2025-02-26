<script setup lang="ts">
const method = defineModel();
</script>
<template>
  <div class="form-control">
    <h4 class="label-text">Method:</h4>
    <label class="label cursor-pointer flex justify-start">
      <input
        v-model="method"
        type="radio"
        name="method"
        value="get"
        class="radio radio-primary"
      />
      <span class="label-text ml-2">GET</span>
    </label>
    <label class="label cursor-pointer flex justify-start">
      <input
        v-model="method"
        type="radio"
        name="method"
        value="post"
        class="radio radio-primary"
      />
      <span class="label-text ml-2">POST</span>
    </label>
  </div>
</template>
