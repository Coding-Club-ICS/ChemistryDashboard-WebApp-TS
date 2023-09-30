<template>
  <div class="w-full flex flex-col justify-between">
    <h1 class="font-semibold text-[#D8D2C0] text-[31px] mx-auto">Home</h1>
    <div class="flex justify-between m-auto">
      <h1>{{ elementName }}</h1>
    </div>

  </div>
</template>

<script setup lang="ts">
  import instance from '../api'
  import { ref } from 'vue';

  const elementName = ref('')

  const getProperties = async () => {
    await instance.get('/element/Cl')
    .then((response) => {
      console.log(response);
      elementName.value = response.data.name
    })
    .catch((error) => {
      console.log(error);
    });
  }

  getProperties();
</script>