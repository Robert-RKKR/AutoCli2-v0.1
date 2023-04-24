<script setup lang="ts">
    // SideBarAction import:
</script>

<template>
    <header id="sidebar">

        <nav id="sidebar_menu">

            <ul>
                <li class="main_menu_item">
                    <a href="#" class="main_menu_link">
                        <span class="icon">home</span>
                        <p>Dashboard</p>
                    </a>
                </li>
                <li class="main_menu_item">
                    <a href="#" class="main_menu_link">
                        <span class="icon">settings_applications</span>
                        <p>Administration</p>
                    </a>
                </li>
                <li class="main_menu_item">
                    <a href="#" class="main_menu_link">
                        <span class="icon">dataset</span>
                        <p>Inventory</p>
                    </a>
                    <ul class="main_menu_submenu hidden">
                        <li class="main_menu_subitem">
                            <a href="#" class="main_menu_sublink">
                                <span class="icon">terminal</span>
                                <p>Hosts</p>
                            </a>
                        </li>
                        <li class="main_menu_subitem">
                            <a href="#" class="main_menu_sublink">
                                <span class="icon">terminal</span>
                                <p>Tags</p>
                            </a>
                        </li>
                    </ul>
                </li>
                <li class="main_menu_item">
                    <a href="#" class="main_menu_link">
                        <span class="icon">file_open</span>
                        <p>Templates</p>
                    </a>
                </li>
                <li class="main_menu_item">
                    <a href="#" class="main_menu_link">
                        <span class="icon">terminal</span>
                        <p>Executions</p>
                    </a>
                </li>
            </ul>

        </nav>

        <div id="sidebar_user_menu">
                
            <img src="ico/model/users/business-woman.svg" alt="Menu">
            <div>
                <h3>Robert Kucharski</h3>
                <p>Administrator</p>
            </div>

        </div>
        
    </header>
</template>

<style scoped>
    /*   ----       SIDEBAR        ----   */
    #sidebar {
        display: flex;
        flex-direction: column;
        justify-content	: space-between;
        background: var(--color_second);
        width: 80px;
        overflow: hidden;
        user-select: none;
    }
    
    #page.bigsidebar #sidebar {
        width: 280px;
    }

    /*   ----       MAIN MENU        ----   */
    #sidebar_menu .icon, a {
        color: var(--color_font_second);
    }

    #sidebar_menu .icon {
        font-size: 36px;
        padding: 15px 22px;
    }

    #sidebar_menu {
        flex-grow: 1;
    }

    .main_menu_link {
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    .main_menu_link span {
        padding: 0px 15px;
        font-size: 1.2em;
    }

    .main_menu_link p {
        padding: 0px 15px;
        font-size: 1.2em;
    }

    /*   ----       USER MENU        ----   */
    #sidebar_user_menu {
        display: flex;
        flex-direction: row;
        align-items: center;
    }

    #sidebar_user_menu img {
        width: 40px;
    }

    #sidebar_user_menu > div {
        padding: 0px 15px;
    }
</style>
