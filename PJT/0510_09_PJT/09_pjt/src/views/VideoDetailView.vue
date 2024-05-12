<template>
  <div>
    <h1>동영상 세부</h1>

    <h1>{{ video.snippet.title }}</h1>
    <p>업로드 날짜: {{ publicshedDate }}</p>
    <iframe :src="videoURL" frameborder="0" width="600px" height="400px"></iframe>
    <p>{{ video.snippet.description }}</p>

    <button @click="toggleWatchLater(videoID, video)">
      {{ isvideo ? '동영상 삭제' : '동영상 저장' }}
    </button>

  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router';
import { ref } from 'vue';

const store = useCounterStore()
const route = useRoute()
const videoID = route.params.videoid
const video = store.GetVideo(videoID)
const publicshedDate = formatDate(video.snippet.publishedAt)
const videoURL = `https://www.youtube.com/embed/${videoID}`
const isvideo = ref(store.isLatervideo(videoID))
console.log(video)

function formatDate(dateString) {
  const date = new Date(dateString)
  return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`;
}

function toggleWatchLater() {
  store.toggleWatchLater(videoID, video)
  isvideo.value = store.isLatervideo(videoID)
}

</script>

<style scoped>

</style>