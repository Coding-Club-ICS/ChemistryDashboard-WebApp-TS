<template>
  <div class="w-full flex flex-col gap-[43px]">
    <h1 class="font-semibold text-secondary text-[31px] mx-auto">Calculator</h1>
    <div class="h-full bg-secondary rounded-[15px] px-[100px] py-[64px]">
      <div class="flex flex-col gap-[60px] mx-auto">
        <div class="flex gap-[30px]">
          <input v-model="userEquation" @keyup.enter="balanceEquation" class="flex-1 rounded-full h-[64px] w-full pl-5 placeholder:text-secondary text-secondary caret-secondary bg-primary" type="text" placeholder="Enter the formula..." />
          <button @click="balanceEquation" class="flex justify-center items-center bg-primary w-[64px] h-[64px] rounded-full"><img class="h-[24px] w-auto" src="../assets/search.svg" alt="search"></button>
        </div>
        <h1 class="text-primary text-center font-bold text-[39px]">{{ balancedEquation }}</h1>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue';
  import { instance } from '../api';

  const userEquation = ref('');
  const balancedEquation = ref('');

  const balanceEquation = async () => {
    instance.get(`/balance/${userEquation.value}`)
      .then((res) => {
        balancedEquation.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  }
  


</script>