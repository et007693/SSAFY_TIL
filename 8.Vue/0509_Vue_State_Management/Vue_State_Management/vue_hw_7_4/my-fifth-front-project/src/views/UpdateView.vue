<template>
    <div>
        <h1>데이터 수정 페이지</h1>
        <p>이름: {{ username }}</p>
        <p>잔고: {{ balance.balance }}</p>
        <button @click="store.balanceIncrement(username)">+</button>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const username = useRoute().params.name
const store = useBalanceStore()
const balance = store.balances.find((user) => user.name === username)
const updateBalacne = function() {
    balance
}

</script>

<style scoped>

</style>