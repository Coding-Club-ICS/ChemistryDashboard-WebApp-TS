<template>
  <div class="flex flex-col gap-4 mx-auto">
    <div class="flex flex-col justify-between gap-2">
      <div class="flex justify-between">
        <PeriodicBox v-for="element in elements.slice(1, 3)" :title="element" />
      </div>

      <div class="flex justify-between">
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(3, 5)" :title="element" />
        </div>
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(5, 11)" :title="element" />
        </div>
      </div>

      <div class="flex justify-between gap-4">
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(11, 13)" :title="element" />
        </div>
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(13, 19)" :title="element" />
        </div>
      </div>

      <div class="flex justify-between gap-2">
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(19, 22)" :title="element" />
        </div>
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(22, 37)" :title="element" />
        </div>
      </div>

      <div class="flex justify-between gap-2">
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(37, 40)" :title="element" />
        </div>
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(40, 55)" :title="element" />
        </div>
      </div>

      <div class="flex justify-between gap-2">
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(55, 58)" :title="element" />
        </div>
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(104, 119)" :title="element" />
        </div>
      </div>

      <div class="flex justify-between gap-2">
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(87, 90)" :title="element" />
        </div>
        <div class="flex justify-between gap-2">
          <PeriodicBox v-for="element in elements.slice(90, 105)" :title="element" />
        </div>
      </div>
    </div>

    <div class="flex flex-col gap-2 mx-auto">
      <div class="flex gap-2">
        <PeriodicBox v-for="element in elements.slice(58, 72)" :title="element" />
      </div>
      <div class="flex gap-2">
        <PeriodicBox v-for="element in elements.slice(90, 104)" :title="element" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import instance from '../api'
  import PeriodicBox from './PeriodicBox.vue';
  import { ref } from 'vue';

  const elements = ref([])

  const getElements = async () => {
    await instance.get('/periodictable')
    .then((response) => {
      console.log(response);
      elements.value = response.data["elements"]
    })
    .catch((error) => {
      console.log(error);
    });
  }

  getElements();
</script>