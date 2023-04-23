<script setup lang="ts">
    // import components:
    import PageContentComponent from './PageContentComponent.vue'
    import SideBarComponent from './SideBarComponent.vue'
</script>

<template>
    <main id="page_bottom">

        <SideBarComponent />
        
        <PageContentComponent />

    </main>
</template>

<style scoped>
    #page_bottom {
        display: flex;
        flex-direction: row;
        height: calc(100vh - 70px);
    }
</style>
