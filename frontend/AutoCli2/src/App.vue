<script setup lang="ts">
  // import components:
  import PageBottomComponent from './components/PageBottomComponent.vue'
  import TopBarComponent from './components/PageTopComponent.vue'
  import LoginComponent from './components/LoginComponent.vue'
  // API key import:
  import { apiKey } from './settings';

  // import css:
  import './assets/reset.css'
  import './assets/main.css'
</script>

<template>
  <div v-if="apiKey" id="page" class="bigsidebar">

    <TopBarComponent />

    <PageBottomComponent />
  
  </div>

  <div v-else>
    
    <LoginComponent />

  </div>
</template>

<style>
  @import './assets/reset.css';
  @import './assets/main.css';

  #page {
      display: flex;
      flex-direction: column;
  }
</style>
