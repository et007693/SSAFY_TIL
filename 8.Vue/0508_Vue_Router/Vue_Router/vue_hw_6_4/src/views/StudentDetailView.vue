<template>
    <div>
        <h1>학생 상세 정보 페이지입니다.</h1>
        <p>이름 : {{ username }}</p>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { ref } from 'vue'

const route = useRoute()
const username = ref(route.params.name)

</script>

<style scoped>

</style>