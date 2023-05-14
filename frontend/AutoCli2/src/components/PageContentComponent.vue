<script setup lang="ts">
    import { RouterView } from 'vue-router'
</script>

<template>
    <div id="page_content">
        <main id="content">
            <RouterView />
        </main>
    </div>
</template>

<style scoped>
    #page_content {
        width: calc(100vw - 80px);
        overflow-y: auto;
    }
    
    #page.bigsidebar #page_content {
        width: calc(100vw - 280px);
    }

    #content {
        padding: 30px;
    }
</style>
