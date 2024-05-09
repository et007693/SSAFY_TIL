<template>
    <div>
        <h2>메인 페이지</h2>
        <MainPageVue v-for="balance in balances" :balance="balance"/>
    </div>
</template>

<script setup>
import MainPageVue from '@/components/MainPage.vue';
import { useBalanceStore } from '@/stores/balance';
const store = useBalanceStore()
const balances = store.balances

</script>

<style scoped>

</style>