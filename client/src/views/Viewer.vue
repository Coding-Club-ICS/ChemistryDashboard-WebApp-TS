<template>
  <div class="w-full flex flex-col gap-[43px]">
    <h1 class="font-semibold text-secondary text-[31px] mx-auto">Viewer</h1>
    <div class="h-full bg-secondary rounded-[15px] px-[100px] py-[64px]">
      <div class="flex flex-col gap-[60px] mx-auto">
        <div class="flex gap-[30px]">
          <input v-model="name" @keyup.enter="getCid" class="flex-1 rounded-full h-[64px] w-full pl-5 placeholder:text-secondary text-secondary caret-secondary bg-primary" type="text" placeholder="Enter the compound..." />
          <button @click="getCid" class="flex justify-center items-center bg-primary w-[64px] h-[64px] rounded-full"><img class="h-[24px] w-auto" src="../assets/search.svg" alt="search"></button>
        </div>
        <h1 class="text-primary text-center font-bold text-[39px]">{{ error_message }}</h1>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue';
  import axios from 'axios';

  const name = ref('')
  const error_message = ref('')
  let cid = ''

  const getCid = () => {
    axios.get(`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/${name.value}/cids/JSON`)
    .then((response) => {
      cid = response.data.IdentifierList.CID[0]
      window.open(`https://embed.molview.org/v1/?mode=balls&cid=${cid}`, '_blank')
    })
    .catch((error) => {
      console.log(error);
      error_message.value = "Compound not found."
    });
  }


</script>