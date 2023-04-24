<script setup lang="ts">
  // import components:
  import PageBottomComponent from './components/PageBottomComponent.vue'
  import TopBarComponent from './components/TopBarComponent.vue'

  // import css:
  import './assets/reset.css'
  import './assets/main.css'
</script>

<template>
  <div id="page" class="bigsidebar">

    <TopBarComponent />

    <PageBottomComponent />
  
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
