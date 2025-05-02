<template>
  <div class="w-full flex flex-col items-center justify-center p-8 max-w-3xl mx-auto">
    <div class="flex justify-center mb-8 gap-1">
      <div class="flex group justify-center items-center w-[40px] h-[40px] border-2 border-secondary">
        <h1 class="font-semibold text-secondary text-[16px]">Th</h1>
      </div>
      <div class="flex group justify-center items-center w-[40px] h-[40px] border-2 border-secondary">
        <h1 class="font-semibold text-secondary text-[16px]">Ac</h1>
      </div>
      <div class="flex group justify-center items-center w-[40px] h-[40px] border-2 border-secondary">
        <h1 class="font-semibold text-secondary text-[16px]">N</h1>
      </div>
      <div class="flex group justify-center items-center w-[40px] h-[40px] border-2 border-secondary">
        <h1 class="font-semibold text-secondary text-[16px]">K</h1>
      </div>
      <div class="flex group justify-center items-center w-[40px] h-[40px] border-2 border-secondary">
        <h1 class="font-semibold text-secondary text-[16px]">Y</h1>
      </div>
      <div class="flex group justify-center items-center w-[40px] h-[40px] border-2 border-secondary">
        <h1 class="font-semibold text-secondary text-[16px]">O</h1>
      </div>
      <div class="flex group justify-center items-center w-[40px] h-[40px] border-2 border-secondary">
        <h1 class="font-semibold text-secondary text-[16px]">U</h1>
      </div>
    </div>
    
    <h1 class="font-semibold text-secondary text-[31px] mb-6">Thank You, Teachers!</h1>
    
    <div class="bg-white p-6 rounded-lg shadow-md w-full">
      <p class="text-secondary text-lg mb-4">Dear Teachers,</p>
      
      <p class="text-secondary text-lg mb-4">
        Thank you for your dedication to teaching chemistry and inspiring the next generation of scientists.
        Your guidance, patience, and enthusiasm have made learning this subject both engaging and accessible.
      </p>
      
      <p class="text-secondary text-lg mb-4">
        We deeply appreciate the countless hours you've spent preparing lessons, answering questions, 
        and helping students understand complex concepts. Your commitment to education makes a profound 
        difference in your students' lives.
      </p>
      
      <p class="text-secondary text-lg mb-4">
        This Chemistry Dashboard was created with your needs in mind, and we hope it serves as a valuable 
        resource in your classroom. Your feedback and suggestions have been instrumental in shaping this tool.
      </p>
      
      <p class="text-secondary text-lg mb-6">
        With sincere gratitude,<br>
        DongJin
      </p>
      
      <div class="text-center">
        <router-link to="/" class="bg-secondary text-white px-6 py-2 rounded-md hover:opacity-90 transition-opacity inline-block">
          Return to Dashboard
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.element-box {
  border: 2px solid #3b82f6;
  border-radius: 4px;
  padding: 6px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f9ff;
  width: 60px;
  height: 70px;
  font-family: sans-serif;
}

.atomic-number {
  font-size: 10px;
  text-align: left;
  width: 100%;
  color: #1e40af;
}

.symbol {
  font-size: 24px;
  font-weight: bold;
  color: #1d4ed8;
}

.name {
  font-size: 9px;
  color: #1e40af;
  text-align: center;
}

@media (max-width: 640px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, auto);
  }
  
  .element-box {
    width: 50px;
    height: 60px;
  }
  
  .symbol {
    font-size: 20px;
  }
}
</style>
