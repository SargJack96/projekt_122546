<script setup lang="tsx">
import { defineAsyncComponent } from 'vue';
import Loader from './Loader.vue';
import Students from '@/components/Students.vue';
const timeout = (ms:any) => new Promise(resolve => setTimeout(resolve, ms));
// const Students = defineAsyncComponent({
//   loader:() => import('@/components/Students.vue'),
//   loadingComponent: () => Loader,
//   errorComponent: () => 'Wystąpił błąd podczas ładowania komponentu',
//   timeout: 3000,
// })
</script>

<template>
  <h1>Lista studentów</h1>
  <div id="column_names">
      <span>Imię</span>
      <span>Nazwisko</span>
      <span>Kierunek</span>
      <span>Indeks</span>
      <span>Grupa</span>
  </div>
  <Students />
</template>

<style scoped>
  h1 {
    text-align: center;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
  }
  #column_names {
    display: flex;
    justify-content: center;
    width: 100%;
    padding: 1rem;
    border-bottom: 1px solid var(--color-border);
    background-color: var(--vt-c-black-soft);
    
  }
  #column_names span {
    width: 20%;
    font-weight: 700;
  }

</style>
