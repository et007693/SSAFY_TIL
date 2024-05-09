<template>
    <div>
        <h3>자식 페이지</h3>
        <p>{{ children.name }}</p>
    </div>
</template>

<script setup>
const {post} = defineProps ({
    children: Object
})
</script>

<style scoped>

</style>