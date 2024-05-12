<template>
  <div class="video-list">
    <div v-for="later in watchLater" class="video-card" @click="videodetail(video.id.videoId)">
      <img :src="later.detail.snippet.thumbnails.default.url" alt="" class="video-image">
      <p>{{ later.detail.snippet.title }}</p>
      <p>{{ later.detail.snippet.channelTitle }}</p>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
const watchLater = store.watchLater
console.log(watchLater)

</script>

<style scoped>
.video-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.video-card {
  width: 200px;
  border: 1px solid #ccc;
  border-radius: 5%;
  padding: 10px;
}

.video-image {
  width: 100%;
}
</style>