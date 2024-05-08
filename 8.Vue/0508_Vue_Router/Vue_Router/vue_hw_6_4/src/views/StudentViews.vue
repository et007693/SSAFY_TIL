<template>
    <div>
        <h1>학생 상세 정보 목록입니다.</h1>
        <p v-for="student in students" @click="detail(student.name)">{{ student.name }} 학생 정보 보기</p>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
const students = ref([
    {name : '김하나'},
    {name : '김두리'},
    {name : '김서이'},
])
const router = useRouter()
const detail = function(studentname) {
    router.push({ name: 'detail', params: { name: studentname }})
}
</script>

<style scoped>

</style>