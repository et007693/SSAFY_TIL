<template>
    <div>
        <h3>{{ $route.params.username }}이 작성한 게시글</h3>
        <ol>
            <PostListItem v-for="post in posts" :post="post" :key="post.id"></PostListItem>
        </ol>
        <hr>
        <RouterView />
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
import PostListItem from '@/components/PostListItem.vue'

let id = 1
const posts = ref([
    { id: id++, title: 'Post 1', content: 'Content 1'},
    { id: id++, title: 'Post 2', content: 'Content 2'},
    { id: id++, title: 'Post 3', content: 'Content 3'},
])
</script>

<style scoped>

</style>