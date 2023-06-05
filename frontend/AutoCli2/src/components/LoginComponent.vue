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
            <div id="login_top">
                <h2>Login</h2>
            </div>
            <div id="login_content">
                <form @submit.prevent="submitForm">
                    <div class="login_field">
                        <label for="username">Username</label>
                        <input type="text" id="username" v-model="username" required>
                    </div>
                    <div class="login_field">
                        <label for="password">Password</label>
                        <input type="password" id="password" v-model="password" required>
                    </div>
                    <div class="login_field">
                        <button @click="collectApiKey()" type="submit">Login</button>
                    </div>
                </form>
            </div>
            <div id="login_bottom">
                <p>AutoCLi - Robert Kucharski</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
    #login_page {
        height: 100vh;
        width: 100vw;
        background: #e9e9e9;
    }

    #login_box {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: #ffffff;
        box-shadow: 0 0.46875rem 2.1875rem rgba(48,48,48,.02), 0 0.6375rem 1.40625rem rgba(48,48,48,.02), 0 0.25rem 0.33125rem rgba(48,48,48,.03), 0 0.125rem 0.1875rem rgba(48,48,48,.02);
        border: 1px solid rgba(26,54,126,.125);
    }

    #login_top {
        background: #1d875b;
        padding: 30px;
        text-transform: uppercase;
        font-size: 1.3em;
    }

    #login_content {
        display: flex;
        flex-direction: column;
        padding: 60px 100px;
    }

    .login_field {
        display: flex;
        flex-direction: column;
    }

    .login_field label {
        font-family: "Alegreya Sans SC", sans-serif;
        font-size: 1.2em;
        margin: 6px;
        color: #4c4c4c;
    }

    .login_field input {
        border: 0px;
        padding: 15px 50px;
        margin: 6px;
        background: #e9e9e9;
    }

    .login_field button {
        border: 0px;
        padding: 15px 150px;
        margin: 20px 6px;
        background: #548be9;
    }

    #login_bottom {
        background: #404040;
        padding: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
        color: #e6e6e6;
        font-size: 1em;
    }
</style>
