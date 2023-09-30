<template>
  <div class="w-full flex flex-col justify-between">
    <h1 class="font-semibold text-secondary text-[31px] mx-auto">Home</h1>
    <h1 class="font-medium text-secondary text-[31px] mx-auto">{{ elementName }}</h1>
    <Periodic />
  </div> 

</template>

<script setup lang="ts">
  import instance from '../api'
  import { ref, watch } from 'vue';
  import Periodic from '../components/Periodic.vue'
  import { storeToRefs } from 'pinia';
  import { useElementStore } from '../stores/ElementStore';

  const elements = ref([])
  const elementName = ref('')
  const store = useElementStore();
  const { symbol } = storeToRefs(store);

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

  watch(symbol, async () => {
    await instance.get(`/element/${store.symbol}`)
    .then((response) => {
      console.log(response);
      elementName.value = response.data.name
    })
    .catch((error) => {
      console.log(error);
    });
  })

  getElements();
</script>