<template>
  <div class="w-full flex flex-col justify-between">
    <h1 class="font-semibold text-secondary text-[31px] mx-auto">Home</h1>
    <h1 class="font-medium text-secondary text-[31px] mx-auto">Hydrogen</h1>
    <Periodic />
  </div> 

</template>

<script setup lang="ts">
  import instance from '../api'
  import { ref } from 'vue';
  import Periodic from '../components/Periodic.vue'

  const elements = ref([])
  const elementName = ref('')

  const getElements = async () => {
    await instance.get('/periodictable')
    .then((response) => {
      console.log(response);
      elements.value = response.data["elements"]
      console.log(elements.value[8])
    })
    .catch((error) => {
      console.log(error);
    });
  }

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

  getElements();
  getProperties();
</script>