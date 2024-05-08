<template>
  <MainPage />
  <RouterLink :to="{ name: 'some' }">Some</RouterLink>
  <span> | </span>
  <RouterLink :to="{ name: 'other' }">Other</RouterLink>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainPage from '@/components/MainPage.vue'

</script>

<style scoped>

</style>
