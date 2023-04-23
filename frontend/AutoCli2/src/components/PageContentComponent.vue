<script setup lang="ts">
    import { RouterView } from 'vue-router'
</script>

<template>
    <div id="page_content">
        <RouterView />
    </div>
</template>

<style scoped>
    #page_content {
        width: calc(100vw - 80px);
    }

    #page.bigsidebar #page_content {
        width: calc(100vw - 280px);
    }
</style>
