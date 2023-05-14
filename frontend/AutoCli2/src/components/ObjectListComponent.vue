<script setup lang="ts">
    // Axios import:
    import axios from 'axios'

    // Collect host data:
    const apiKey = '28befc9a9922fa6644c7fd70d5ee5fcd51246823';
    const config = {
        headers: {
            'Authorization': `Token ${apiKey}`}}
    const response = await axios.get('http://127.0.0.1:8000/api-inventory/full-host/', config)
    const collectedData = response.data.page_results
</script>

<template>
    <div class="box_container">

        <article v-for="host in collectedData" :key="host.pk" class="box_item">
            <!-- <div class="box_item_head"></div> -->
            <div class="box_item_body">
                <h3>{{ host.name }}</h3>
                <q>{{ host.hostname }}</q>
                <ul>
                    <li>Created: {{ host.created }}</li>
                    <li>Updated: {{ host.updated }}</li>
                    <li v-if="host.site">Site: {{ host.site.name }}</li>
                    <li>Platform: {{ host.platform.name }}</li>
                    <li>Credential: {{ host.credential.name }}</li>
                    <li>SSH port: {{ host.ssh_port }}</li>
                    <li>HTTP port: {{ host.http_port }}</li>
                    <li>Certificate check: {{ host.certificate_check }}</li>
                </ul>
            </div>
            <!-- <div class="box_item_footer"></div> -->
        </article>

    </div>
</template>

<style scoped>
    .box_container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-column-gap: 20px;
        grid-row-gap: 20px;
        justify-items: stretch;
        align-items: center;
    }

    .box_item {
        background: #e9e9e9;
        box-shadow: 5px 5px 20px 1px rgba(46,35,94,.07);
        box-shadow: -5px -5px 20px 1px rgba(46,35,94,.07);
    }

    .box_item_head,
    .box_item_body,
    .box_item_footer {
        padding: 30px;
    }
</style>