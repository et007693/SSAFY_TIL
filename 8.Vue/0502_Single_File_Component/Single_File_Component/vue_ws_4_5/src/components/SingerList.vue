<template>
  <h1 style="text-align: center; color: red;">가수 목록</h1>
    <div style="display: inline-block; text-align: center;">
      <SingerDetail v-for="singer in singers" class="card"/>
    </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue';
import { ref } from 'vue'

const singers = ref([
  {name :'adele'},
  {name :'maroon 5'},
  {name :'Dua Lipa'},
])

</script>

<style lang="scss" scoped>
.card {
  display: inline-block;
  width: 40%;
  margin: 20px;
  white-space: nowrap;
}

h1 {
  color: orangered;
}
</style>