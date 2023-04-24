<script setup lang="ts">
    // VUE import:
    import { ref } from 'vue'

    // import logo:
    import LogoSVG from '../assets/logo.svg'

    const sideBarAction = ref(false)
</script>

<template>
    <div id="topbar_logo">
        <img id="page_logo" :src="LogoSVG" alt="Menu">
        <h1 id="page_title">AutoCLI 2</h1>
        <span class="icon">read_more</span>
    </div>
</template>

<style scoped>
    #topbar_logo {
        height: 70px;
        background: var(--color_first);
        display: flex;
        flex-direction: row;
        align-items: center;
        width: 280px;
    }

    #page_logo {
        width: 50px;
        padding: calc((70px - 36.563px) / 2) 15px;
        fill: var(--color_second);
    }

    #page_title {
        font-size: 1.8em;
        padding: 0px 15px;
        color: var(--color_font_third);
    }

    #topbar_logo .icon {
        color: var(--color_font_third);
    }
</style>
