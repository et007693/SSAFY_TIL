<template>
    <div>
        <h2>부모 컴포넌트</h2>
        <p>{{ family.father }}</p>
        <p>{{ family.mother }}</p>
        <ChildPage v-for="children in family.children" :children="children" />
    </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';
const {post} = defineProps ({
    family: Object
})
// console.log(family)
</script>

<style scoped>

</style>