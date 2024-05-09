<template>
    <div>
        <p>이름: {{ balance.name }}</p>
        <p>잔고: {{ balance.balance }}</p>
        <button @click="goUpdate(balance.name)">updateBalance</button>
        <hr>
    </div>
</template>

<script setup>
import router from '@/router';

    const {post} = defineProps({
        balance: Object
    })

    const goUpdate = function(name) {
        router.push({ name: 'update', params: { name: name } })
    }

</script>

<style scoped>

</style>