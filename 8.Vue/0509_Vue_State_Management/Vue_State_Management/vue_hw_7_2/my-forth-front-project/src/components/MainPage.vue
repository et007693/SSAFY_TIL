<template>
    <div>
        <h1>pinia 연습하기</h1>
        <ParentPageVue v-for="family in familyInfo" :family="family"/>
    </div>
</template>

<script setup>
import { useFamilyStore } from '@/stores/family';
import ParentPageVue from './ParentPage.vue';

const store = useFamilyStore()
const familyInfo = store.familyinfo

</script>

<style scoped>

</style>