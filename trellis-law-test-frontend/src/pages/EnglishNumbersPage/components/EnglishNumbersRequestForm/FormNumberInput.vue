<script setup lang="ts">
const number = defineModel();
</script>
<template>
  <div class="form-control">
    <label for="number-input" class="label">Number:</label>
    <input
      id="number-input"
      v-model="number"
      type="number"
      name="number"
      min="0"
      max="999999999999999"
      required
      placeholder="Enter a number"
      class="input input-bordered w-full"
    />
  </div>
</template>
