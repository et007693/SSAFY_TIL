<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <RouterLink :to="{ name: 'main' }">main</RouterLink>
  <h1>pinia + router 연습하기</h1>
  <RouterView />
  
</template>

<style scoped>

</style>
