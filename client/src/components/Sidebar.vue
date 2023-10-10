<template>
  <div class="flex flex-col justify-between h-full gap-[43px] w-fit">
    <div class="flex gap-x-2">
      <img src="../assets/flask.svg" alt="flask" class="h-[32px]">
      <p class="text-secondary font-extrabold text-[25px]">Chemix</p>
    </div>
    <div class="flex py-[75%] w-[60px] h-full bg-secondary rounded-[15px] mx-auto">
      <div class="flex flex-col justify-between mx-auto">
        <router-link to="/"><img src="../assets/house.svg" alt="home" class="h-[32px] mx-auto"></router-link>
        <router-link to="/calculator"><img src="../assets/calculator.svg" alt="home" class="h-[32px] mx-auto"></router-link>
        <router-link to="viewer"><img src="../assets/cube.svg" alt="home" class="h-[32px] mx-auto"></router-link>
      </div>
    </div>

  </div>
</template>