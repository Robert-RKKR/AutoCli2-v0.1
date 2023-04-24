<script setup lang="ts">
    // VUE import:
    import { ref } from 'vue'

    // Notifications:
    const notifications_status = ref(false)
    var notifications_active = ref(false)
    var notifications = ref([])
    var socket = new WebSocket("ws://127.0.0.1:8000/ws/notification/");
    socket.onmessage = function(event) {
        var collect = event.data;
        var collected_notification = JSON.parse(collect)
        notifications.value.push(collected_notification)
        console.log(collected_notification.severity)
        notifications_active.value = true
    }
    const changeNotificationStatus = () => {
        notifications_status.value = !notifications_status.value
    }
</script>

<template>
    <div id="topbar_notifications">
        <span v-if="notifications_active" @click="changeNotificationStatus" class='icon'>mark_email_unread</span>
        <span v-else @click="changeNotificationStatus" class='icon'>mail</span>

        <div v-if="notifications_status" id="notifications_list">

            <div id="notifications_list_header">
                <h3>Notifications</h3>
                <a href="#">Marks all as read</a>
            </div>

            <div v-if="notifications.length > 0" id="notifications_list_body">
                <a v-for="notification in notifications" class="notification_item blue">
                    <div class="notification_icon">
                        <span v-if="notifications.severity === 1" class='icon red'>report</span>
                        <span v-else-if="notifications.severity === 2" class='icon violet'>error</span>
                        <span v-else-if="notifications.severity === 3" class='icon yellow'>warning</span>
                        <span v-else-if="notifications.severity === 4" class='icon blue'>circle_notifications</span>
                    </div>
                    <span>{{ notification.message }}</span>
                </a>
            </div>

            <div v-else id="notifications_empty">
                <span class='icon'>unsubscribe</span>
            </div>

            <div id="notifications_list_footer">
                <a href="#">View All Notifications</a>
            </div>

        </div>
    </div>
</template>

<style scoped>
    .icon {
        cursor: pointer;
    }

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
        background: #e5e5e5;
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

    #notifications_empty .icon {
        font-size: 3em;
        color: var(--color_light_red)!important;
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
        background: #e5e5e5;
    }
    #topbar_notifications .icon {
        color: var(--color_font_third);
    }
</style>
