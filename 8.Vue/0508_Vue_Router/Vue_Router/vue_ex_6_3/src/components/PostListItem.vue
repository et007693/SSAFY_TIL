<template>
    <div>
        <li>
            <RouterLink :to="{ name: 'post-detail', params: {'id':post.id} }">제목: {{ post.title }}</RouterLink>
        </li>
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
const {post} = defineProps({
    post: Object
})

</script>

<style scoped>

</style>