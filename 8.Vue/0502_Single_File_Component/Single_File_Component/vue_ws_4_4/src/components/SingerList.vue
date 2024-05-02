<template>
  <h1 style="text-align: center; color: red;">가수 목록</h1>
  <div style="text-align: center;">
    <SingerDetail class="card" />
    <SingerDetail class="card" />
    <SingerDetail class="card" />
  </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue';

</script>

<style lang="scss" scoped>
.card {
  display: inline-block;
  width: 40%;
  margin: 20px;
  text-align: center;
}

h1 {
  color: orangered;
}
</style>