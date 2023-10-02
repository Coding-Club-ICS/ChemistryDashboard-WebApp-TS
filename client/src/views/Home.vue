<template>
  <div class="w-full flex flex-col justify-between">
    <h1 class="font-semibold text-secondary text-[31px] mx-auto">Home</h1>
    <div class="flex justify-between gap-8 mx-auto">
      <h1 class="font-medium text-secondary text-[31px]">{{ elementName || '' }}</h1>
      <div class="flex gap-2">
        <div class="flex flex-col gap-2 mx-auto">
          <h1 class="text-secondary text-[16px]">Atomic Mass</h1>
          <p class="text-secondary text-[13px] text-center">{{ elementMass || '' }}</p>
        </div>
        <div class="flex flex-col gap-2 mx-auto">
          <h1 class="text-secondary text-[16px]">Atmoic Radius</h1>
          <p class="text-secondary text-[13px] text-center">{{ elementRadius || '' }}</p>
        </div>
      </div>
    </div>
    <Periodic />
  </div> 

</template>

<script setup lang="ts">
  import { ref, watch } from 'vue';
  import Periodic from '../components/Periodic.vue'
  import { storeToRefs } from 'pinia';
  import { useElementStore } from '../stores/ElementStore';
  import * as Element_Data from '../data/data.json'

  let elementName = ref('')
  let elementMass = ref('') 
  let elementRadius = ref('')
  const store = useElementStore();
  const { symbol } = storeToRefs(store);

  watch(symbol, async () => {
    elementName.value = Element_Data[store.symbol as keyof typeof Element_Data].name
    elementMass.value = Element_Data[store.symbol as keyof typeof Element_Data].atomic_weight.toString()
    elementRadius.value = Element_Data[store.symbol as keyof typeof Element_Data].atomic_radius.toString()
    console.log(elementName)
    console.log(elementMass)
    console.log(elementRadius)
  })

</script>