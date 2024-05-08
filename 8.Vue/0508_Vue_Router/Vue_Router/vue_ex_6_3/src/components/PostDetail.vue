<template>
    <div>
        <p>번호 : {{ post.id }}</p>
        <p>제목 : {{ post.title }}</p>
        <p>내용 : {{ post.content }}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, onBeforeRouteUpdate } from 'vue-router'

let id = 1
const posts = ref([
    { id: id++, title: 'Post 1', content: 'Content 1'},
    { id: id++, title: 'Post 2', content: 'Content 2'},
    { id: id++, title: 'Post 3', content: 'Content 3'},
])
const route = useRoute()
const postId = ref(route.params.id)
const post = ref(posts.value.find(post => post.id === Number(postId.value)))

onBeforeRouteUpdate((to,from)=>{
    post.value = posts.value.find(post => post.id === Number(to.params.id))
})

</script>

<style scoped>

</style>