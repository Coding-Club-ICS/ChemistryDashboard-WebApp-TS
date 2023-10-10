<template>
  <button @click="store.setSymbol(title!)" class="flex group focus:bg-secondary justify-center items-center w-[40px] h-[40px] border-2 border-secondary"><h1 class="font-semibold text-secondary group-focus:text-primary text-[16px]">{{ title }}</h1></button>

</template>

<script setup lang="ts">
  import { useElementStore } from "../stores/ElementStore"

  const store = useElementStore();

  defineProps({
    title: String,
  })


</script>