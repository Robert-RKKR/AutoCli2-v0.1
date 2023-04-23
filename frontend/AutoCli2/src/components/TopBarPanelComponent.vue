<script setup lang="ts">
    // import components:
    import NotificationComponent from './NotificationComponent.vue'
</script>

<template>
    <div id="topbar_panel">
        <div id="topbar_search">
            <input type="search" id="site_search" placeholder="Search on the site..." name="q">
        </div>

        <div id="topbar_title">
            <h2>Add a new device</h2>
        </div>
            
        <div id="topbar_menu">

            <div id="topbar_actions">
                <span class='icon'>add_box</span>
                <span class='icon'>backspace</span>
                <span class='icon'>edit_square</span>
                <span class='icon'>file_copy</span>
            </div>

            <NotificationComponent />

            <div id="topbar_dark_mode">
                <span class='icon dark_mode_on'>toggle_on</span>
                <span class='icon dark_mode_off hidden'>toggle_off</span>
            </div>
        </div>
    </div>
</template>

<style scoped>
    /*   ----       TOPBAR - PANEL        ----   */
    #topbar_panel {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        margin: 0px 30px;
        width: calc(100vw - 280px);
    }

    /*   ----       TOPBAR - TITLE        ----   */
    #topbar_title {
        font-size: 1.6em;
        color: var(--color_font_third);
    }

    /*   ----       TOPBAR - SEARCH        ----   */
    #site_search {
        border: none;
        padding: 6px 30px;
        width: 100%;
        text-align: center;
        background: rgba(255, 255, 255, 0.182);
    }

    #site_search::placeholder {
        color: var(--color_font_third);
    }

    #site_search:focus {
        outline: none;
        background: rgba(255, 255, 255, 0.182);
        color: var(--color_font_third);
    }

    /*   ----       TOPBAR - MENU        ----   */
    #topbar_menu {
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    #topbar_menu .icon {
        color: var(--color_font_third);
    }

    #topbar_menu > div {
        padding-left: 30px;
    }
</style>
