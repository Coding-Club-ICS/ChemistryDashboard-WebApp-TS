<template>
  <div class="flex flex-col gap-4 mx-auto">
    <div class="flex flex-col justify-between gap-2">
      <div class="flex justify-between">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[1] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[2] }}</h1></div>
      </div>

      <div class="flex justify-between">
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[3] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[4] }}</h1></div>
        </div>
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[5] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[6] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[7] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[8] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[9] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[10] }}</h1></div>
        </div>
      </div>

      <div class="flex justify-between gap-4">
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[11] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[12] }}</h1></div>
        </div>
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[13] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[14] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[15] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[16] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[17] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[18] }}</h1></div>
        </div>
      </div>

      <div class="flex justify-between gap-2">
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[19] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[20] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[21] }}</h1></div>
        </div>
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[22] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[23] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[24] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[25] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[26] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[27] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[28] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[29] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[30] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[31] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[32] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[33] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[34] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[35] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[36] }}</h1></div>
        </div>
      </div>

      <div class="flex justify-between gap-2">
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[37] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[38] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[39] }}</h1></div>
        </div>
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[40] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[41] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[42] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[43] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[44] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[45] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[46] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[47] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[48] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[49] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[50] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[51] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[52] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[53] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[54] }}</h1></div>
        </div>
      </div>

      <div class="flex justify-between gap-2">
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[55] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[56] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[57] }}</h1></div>
        </div>
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[72] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[73] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[74] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[75] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[76] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[77] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[78] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[79] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[80] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[81] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[82] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[83] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[84] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[85] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[86] }}</h1></div>
        </div>
      </div>

      <div class="flex justify-between gap-2">
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[87] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[88] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[89] }}</h1></div>
        </div>
        <div class="flex justify-between gap-2">
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[90] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[91] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[92] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[93] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[94] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[95] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[96] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[97] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[98] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[99] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[100] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[101] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[102] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[103] }}</h1></div>
          <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[104] }}</h1></div>
        </div>
      </div>
    </div>

    <div class="flex flex-col gap-2">
      <div class="flex gap-2">
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[58] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[59] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[60] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[61] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[62] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[63] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[64] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[65] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[66] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[67] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[68] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[79] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[80] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[81] }}</h1></div>
      </div>
      <div class="flex gap-2">
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[90] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[91] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[92] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[93] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[94] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[95] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[96] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[97] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[98] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[99] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[100] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[101] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[102] }}</h1></div>
        <div v-bind:class="styles.box"><h1 v-bind:class="styles.text">{{ elements[103] }}</h1></div>
      </div>
    </div>


  </div>
  
</template>

<script setup lang="ts">
  import instance from '../api'
  import { ref } from 'vue';

  const elements = ref([])

  const styles = ref({
    box: "flex justify-center items-center w-[40px] h-[40px] border-2 border-secondary",
    text: "font-semibold text-secondary text-[16px]"
  })

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

  getElements();
</script>