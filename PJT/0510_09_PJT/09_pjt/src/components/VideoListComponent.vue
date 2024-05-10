<template>
  <div class="video-list">
    <div v-for="video in videos" class="video-card" @click="videodetail(video.id.videoId)">
      <img :src="video.snippet.thumbnails.default.url" alt="" class="video-image">
      <p>{{ video.snippet.title }}</p>
      <p>{{ video.snippet.channelTitle }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import router from '@/router'

const store = useCounterStore()
const videos = store.videos

const videodetail = function(videoid) {
  router.push({ name:'detail', params: { videoid:videoid }})
}

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