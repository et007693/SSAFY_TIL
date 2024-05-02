<template>
  <div style="border: 1px solid black; text-align: center;">
    <h1>가수 이름</h1>
    <img class="singer-img" src="@/assets/singer.jpg" alt="">
    <p>가수 소개글</p>
    <SingerAlbum />
  </div>
</template>

<script setup>
import SingerAlbum from './SingerAlbum.vue';


</script>

<style scoped>

.singer-img {
  width: 50%;
  border-radius: 50%;
}
</style>