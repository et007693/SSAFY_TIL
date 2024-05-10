<template>
  <div>
    <h1>비디오 검색</h1>
    <form @submit.prevent="searchFunction">
      <input type="text" id="searchInput" placeholder="검색어를 입력하세요" v-model="query">
      <button type="submit">검색</button>
    </form>
    <VideoListComponent />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
import VideoListComponent from '@/components/VideoListComponent.vue';

const store = useCounterStore()
const query = ref('')

const apiKey = 'AIzaSyDKnoh7lsnw1Ye9a_5GLDk7VLnHmctBH9E'
const apiUrl = 'https://www.googleapis.com/youtube/v3/search'

const searchFunction = function() {
    const url = `${apiUrl}?key=${apiKey}&part=snippet&type=video&maxResults=30&regionCode=KR&q=${query.value}`
    
    axios({
      method: 'get',
      url: url
    })
    .then((response) => {
      console.log(response)
      store.videos.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

</script>

<style scoped>

</style>