<script setup lang="ts">
import Sidebar from './components/Sidebar.vue';
</script>

<template>
  <router-link to="/" />
  <router-link to="/calculator" />
  <router-link to="/viewer" />

  <div class="h-full">
    <router-view />
    <Sidebar />
  </div>
</template>
