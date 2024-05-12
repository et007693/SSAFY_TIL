<template>
  <div>
    <h1>동영상 세부</h1>
    <h1>{{ video.snippet.title }}</h1>
    <p>업로드 날짜: {{ publicshedDate }}</p>
    <iframe :src="videoURL" frameborder="0" width="600px" height="400px"></iframe>
    <p>{{ video.snippet.description }}</p>

    <button @click="toggleWatchLater">
      {{ isVideoInWatchLater ? '동영상 삭제' : '동영상 저장' }}
    </button>

  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router';
import { ref } from 'vue'

const store = useCounterStore()
const route = useRoute()
const videoID = route.params.videoid
const video = store.GetVideo(videoID)
const publicshedDate = formatDate(video.snippet.publishedAt)
const videoURL = `https://www.youtube.com/embed/${videoID}`
const watchLater = store.watchLater.value
console.log(watchLater)

function formatDate(dateString) {
  const date = new Date(dateString)
  return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`;
}

function toggleWatchLater() {
  const isVideoInWatchLater = ref(watchLater.value.find(video => video === videoID))
  if (isVideoInWatchLater) {
    const idx = watchLater.value.findIndex(video => video === videoID)
    watchLater.value.splice(idx, 1)
  } else {
    watchLater.value.push(videoID)
  }
}
// const tempt = watchLater.find(video => video.id.videoId === videoID)
// console.log(tempt)
// console.log(video.snippet.publishedAt)
</script>

<style scoped>

</style>