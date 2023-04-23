<script setup lang="ts">
    var socket = new WebSocket("ws://127.0.0.1:8000/ws/notification/");
    socket.onmessage = function(event) {
        var collect = event.data;
        const notification = JSON.parse(collect)
    }
</script>

<template>
    <div id="topbar_notifications">
        <span class='icon notifications_on'>mail</span>
        <span class='icon notifications_off hidden'>mark_email_unread</span>

        <div id="notifications_list" class="hidden">

            <div id="notifications_list_header">
                <h3>Notifications</h3>
                <a href="#">Marks all as read</a>
            </div>

            <div id="notifications_list_body">
                <a class="notification_item green">
                    <div class="notification_icon">
                        <span class='icon'>info</span>
                    </div>
                    <span>Process of collecting information from all requested devices has been accomplish.</span>
                </a>
                <a class="notification_item violet">
                    <div class="notification_icon">
                        <span class='icon'>error</span>
                    </div>
                    <span>Process of collecting information from all requested devices has been accomplish (Successfully collected data from 15 devices out of 16 requested devices in 45,55 seconds).</span>
                </a>
                <a class="notification_item yellow">
                    <div class="notification_icon">
                        <span class='icon'>warning</span>
                    </div>
                    <span>Process of collecting information from all requested devices has been accomplish.</span>
                </a>
                <a class="notification_item blue">
                    <div class="notification_icon">
                        <span class='icon'>circle_notifications</span>
                    </div>
                    <span>Process of collecting information from all requested devices has been accomplish (Successfully collected data from 15 devices out of 16 requested devices in 45,55 seconds).</span>
                </a>
                <a class="notification_item red">
                    <div class="notification_icon">
                        <span class='icon'>report</span>
                    </div>
                    <span>Process of collecting information from all requested devices has been accomplish.</span>
                </a>
            </div>

            <div id="notifications_empty" class="hidden">
                <span class='icon'>unsubscribe</span>
            </div>

            <div id="notifications_list_footer">
                <a href="#">View All Notifications</a>
            </div>

        </div>
    </div>
</template>

<style scoped>
    #notifications_list {
        position: absolute;
        user-select: none;
        top: 70px;
        right: 20px;
        width: 400px;
        z-index: 1001;
    }

    #notifications_list h3, a {
        color: var(--color_font_first);
    }

    #notifications_list_header {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding: 20px;
        background: var(--color_third);
    }

    #notifications_empty,
    #notifications_list_body {
        padding: 20px;
        background: #f7f7f7;
        display: flex;
        flex-direction: column;
        max-height: 250px;
        overflow-y: auto;
    }

    #notifications_empty {
        flex-direction: row;
        justify-content: center;
    }

    .notification_item {
        display: flex;
        flex-direction: row;
        align-items: center;
        cursor: pointer;
    }

    .notification_item:not(:last-child) {
        margin-bottom: 20px;
    }

    .notification_icon {
        font-size: 20px;
        padding: 15px;
        border-radius: 10em;
        margin-right: 20px;
    }

    #notifications_empty .icon {
        font-size: 3em;
        color: var(--color_light_red)
    }

    .notification_item.blue .notification_icon {
        background: var(--color_light_blue);
    }

    .notification_item.red .notification_icon {
        background: var(--color_light_red);
    }

    .notification_item.yellow .notification_icon {
        background: var(--color_light_yellow);
    }

    .notification_item.violet .notification_icon {
        background: var(--color_light_violet);
    }

    .notification_item.green .notification_icon {
        background: var(--color_light_green);
    }

    .notification_item.blue .icon {
        color: var(--color_strong_blue)!important;
    }

    .notification_item.red .icon {
        color: var(--color_strong_red)!important;
    }

    .notification_item.yellow .icon {
        color: var(--color_strong_yellow)!important;
    }

    .notification_item.violet .icon {
        color: var(--color_strong_violet)!important;
    }

    .notification_item.green .icon {
        color: var(--color_strong_green)!important;
    }

    #notifications_list_footer {
        padding: 20px;
        background: var(--color_third);
    }
    #topbar_notifications .icon {
        color: var(--color_font_third);
    }
</style>
