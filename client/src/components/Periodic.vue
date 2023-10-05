<template>
  <div class="flex flex-col gap-4 mx-auto">
    <div class="flex flex-col justify-between gap-2">
      <div class="flex justify-between">
        <PeriodicBox v-for="element in elements.slice(1, 3)" :title="element" />
      </div>

      <div class="flex justify-between">
        <div class="flex gap-2">
          <PeriodicBox v-for="element in elements.slice(3, 5)" :title="element" />
        </div>
        <div class="flex gap-2">
          <PeriodicBox v-for="element in elements.slice(5, 11)" :title="element" />
        </div>
      </div>

      <div class="flex justify-between">
        <div class="flex gap-2">
          <PeriodicBox v-for="element in elements.slice(11, 13)" :title="element" />
        </div>
        <div class="flex gap-2">
          <PeriodicBox v-for="element in elements.slice(13, 19)" :title="element" />
        </div>
      </div>

      <div class="flex gap-2">
        <PeriodicBox v-for="element in elements.slice(19, 37)" :title="element" />
      </div>

      <div class="flex gap-2">
        <PeriodicBox v-for="element in elements.slice(37, 55)" :title="element" />
      </div>

      <div class="flex gap-2">
        <div class="flex gap-2">
          <PeriodicBox v-for="element in elements.slice(55, 58)" :title="element" />
        </div>
        <div class="flex gap-2">
          <PeriodicBox v-for="element in elements.slice(104, 119)" :title="element" />
        </div>
      </div>

      <div class="flex gap-2">
        <div class="flex gap-2">
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
  import PeriodicBox from './PeriodicBox.vue';

  const elements = 
  ['n', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 
'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']

</script>