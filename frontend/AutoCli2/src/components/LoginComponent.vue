<script setup lang="ts">
    // Vue import:
    import { ref } from 'vue'
    // Axios import:
    import axios from 'axios'
    // API key import:
    import { apiKey } from '../settings';

    // Login data:
    const username = ref('')
    const password = ref('')

    const collectApiKey = async () => {    
        const loginData = {
            username: username.value,
            password: password.value
        }
        const config = {
            headers: {
                'Content-Type': 'application/json'}}
        const response = await axios.post(
            'http://127.0.0.1:8000/api-admin/token-generate/', loginData, config
        ).then(response => {
            apiKey.value = response.data.token
        }).catch(error => {
            console.log(error)
        })
    }
</script>

<template>
    <div id="login_page">
        <div id="login_box">
            <h2>Login</h2>
            <form @submit.prevent="submitForm">
                <div>
                    <label for="username">Username:</label>
                    <input type="text" id="username" v-model="username" required>
                </div>
                <div>
                <label for="password">Password:</label>
                    <input type="password" id="password" v-model="password" required>
                </div>
                <div>
                    <button @click="collectApiKey()" type="submit">Login</button>
                </div>
            </form>
        </div>
    </div>
</template>

<style scoped>
    #login_page {
        height: 100vh;
        width: 100vw;
        background: rgb(150, 150, 150);
    }
</style>
