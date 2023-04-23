<script setup lang="ts">
    // import components:
    import TopBarPanelComponent from './TopBarPanelComponent.vue'
    import LogoComponent from './LogoComponent.vue'
</script>

<template>
    <aside id="topbar">

        <LogoComponent />
        
        <TopBarPanelComponent />

    </aside>
</template>

<style scoped>
    #topbar {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        background: var(--color_first);
        height: 70px;
        width: 100vw;
        user-select: none;
    }

    #page.bigsidebar #sidebar {
        width: 280px;
    }
</style>
